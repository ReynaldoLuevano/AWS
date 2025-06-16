import os
from urllib import response
from datetime import date
from flask import Flask, session, render_template, request, redirect, url_for, flash
from boto3 import client
from dotenv import load_dotenv
import dynamodb_handler as dynamodb
import cloudfront_distribution as cf
import datetime as dt
from flask_awscognito import AWSCognitoAuthentication
import configparser

load_dotenv()
app = Flask(__name__)
app.secret_key = os.urandom(24)
app = Flask(__name__)

config = configparser.ConfigParser()
config.read(r'config.txt')

print(config.get('PARAMS_DETAILS', 'AWS_BUCKET_NAME'))
BUCKET_NAME = config.get('PARAMS_DETAILS', 'AWS_BUCKET_NAME')
CLOUDFRONT_URL = config.get('PARAMS_DETAILS', 'AWS_CLOUDFRONT_URL')

app.config['AWS_DEFAULT_REGION'] = config.get(
    'PARAMS_DETAILS', 'AWS_DEFAULT_REGION')
app.config['AWS_COGNITO_DOMAIN'] = config.get(
    'PARAMS_DETAILS', 'AWS_COGNITO_DOMAIN')
app.config['AWS_COGNITO_USER_POOL_ID'] = config.get(
    'PARAMS_DETAILS', 'AWS_COGNITO_USER_POOL_ID')
app.config['AWS_COGNITO_USER_POOL_CLIENT_ID'] = config.get(
    'PARAMS_DETAILS', 'AWS_COGNITO_USER_POOL_CLIENT_ID')
app.config['AWS_COGNITO_USER_POOL_CLIENT_SECRET'] = config.get(
    'PARAMS_DETAILS', 'AWS_COGNITO_USER_POOL_CLIENT_SECRET')
app.config['AWS_COGNITO_REDIRECT_URL'] = config.get(
    'PARAMS_DETAILS', 'AWS_COGNITO_REDIRECT_URL')

app.config['SECRET_KEY'] = os.urandom(24)
aws_auth = AWSCognitoAuthentication(app)

# MAIN

@app.route("/dashboard")
def dashboard():
    return render_template("home.html", home=True)


@app.route("/viewaccount", methods=["GET", "POST"])
def viewaccount():
    if 'token' not in session:
        return redirect(url_for('login'))
    if session['usert'] == 'customer':
        if request.method == "POST":
            acc_id = request.form.get("acc_id")
            cust_id = request.form.get("cust_id")
            items = {}
            if (acc_id != ""):
                response = dynamodb.getAccountDetailsByAcctId(int(acc_id))
                items = response['Items']
            else:
                items = dynamodb.getAccountDetailsByCustId(cust_id)

            print('data', items)
            if items:
                return render_template('viewaccount.html', viewaccount=True, data=items)
            flash("Account not found! Please,Check you input.", 'danger')
    else:
        flash("You don't have access to this page", "warning")
        return redirect(url_for('dashboard'))
    return render_template('viewaccount.html', viewaccount=True)


@app.route("/viewaccountstatus", methods=["GET", "POST"])
def viewaccountstatus():
    if 'token' not in session:
        return redirect(url_for('login'))
    return render_template('viewaccountstatus.html', viewaccountstatus=True)

# Code for deposit amount


@app.route('/deposit', methods=['GET', 'POST'])
@app.route('/deposit/<acc_id>', methods=['GET', 'POST'])
def deposit(acc_id=None):
    if 'token' not in session:
        return redirect(url_for('login'))
    if session['usert'] == "customer":
        print('in get', acc_id)
        if acc_id is None:
            return redirect(url_for('viewaccount'))
        else:
            if request.method == "POST":
                print('in post deposit', acc_id)
                amount = request.form.get("amount")
                print('amount', amount)
                response = dynamodb.getAccountDetailsByAcctId(int(acc_id))
                if response['Items'] is not None:
                    updatedBalance = int(amount) + \
                        int(response['Items'][0]['balance'])
                    result = dynamodb.updateAcctBalance(
                        int(acc_id), updatedBalance)
                    flash(
                        f"{amount} Amount deposited into account: {acc_id} successfully.", 'success')
                    dynamodb.insertTransactions(
                        acc_id, "Amount Deposited", amount)
                else:
                    flash(f"Account not found or Deactivated.", 'danger')
            else:
                response = dynamodb.getAccountDetailsByAcctId(int(acc_id))
                if response['Items'] is not None:
                    return render_template('deposit.html', deposit=True, data=response['Items'])
                else:
                    flash(f"Account not found or Deactivated.", 'danger')

    return redirect(url_for('viewaccount'))

# Code for withdraw amount


@app.route('/withdraw', methods=['GET', 'POST'])
@app.route('/withdraw/<acc_id>', methods=['GET', 'POST'])
def withdraw(acc_id=None):
    if 'token' not in session:
        return redirect(url_for('login'))
    if session['usert'] == "customer":
        if acc_id is None:
            return redirect(url_for('viewaccount'))
        else:
            if request.method == "POST":
                amount = request.form.get("amount")
                response = dynamodb.getAccountDetailsByAcctId(int(acc_id))
                if response['Items'] is not None:
                    if int(response['Items'][0]['balance']) >= int(amount):
                        updatedBalance = int(
                            response['Items'][0]['balance'])-int(amount)
                        result = dynamodb.updateAcctBalance(
                            int(acc_id), updatedBalance)
                        flash(
                            f"{amount} Amount withdrawn from account: {acc_id} successfully.", 'success')
                        dynamodb.insertTransactions(
                            acc_id, "Amount withdrawn", amount)
                    else:
                        flash(f"Account doesn't have sufficient Balance.", 'success')
                        return redirect(url_for('viewaccount'))
                else:
                    flash(f"Account not found or Deactivated.", 'danger')
            else:
                response = dynamodb.getAccountDetailsByAcctId(int(acc_id))
                if response['Items'] is not None:
                    return render_template('withdraw.html', deposit=True, data=response['Items'])
                else:
                    flash(f"Account not found or Deactivated.", 'danger')

    return redirect(url_for('viewaccount'))

# Code for transfer amount using transact_items


@app.route('/transfer', methods=['GET', 'POST'])
@app.route('/transfer/<cust_id>', methods=['GET', 'POST'])
def transfer(cust_id=None):
    print(cust_id)
    src_data = None
    trg_data = None
    if 'token' not in session:
        return redirect(url_for('login'))
    if session['usert'] == "customer":
        if cust_id is None:
            return redirect(url_for('viewaccount'))
        else:
            if request.method == 'POST':
                src_type = request.form.get("src_type")
                trg_type = request.form.get("trg_type")
                amount = int(request.form.get("amount"))
                if src_type != trg_type:
                    response = dynamodb.getAccountDetailsByCustId(cust_id)
                    print('transfer', response)
                    for i in response:
                        res = []
                        for j in i:
                            print('j is', i[j])
                            res.append(i[j])
                        if str('savings') in res:
                            if str('savings') == src_type:
                                src_data = i
                            else:
                                trg_data = i

                        if str('checking') in res:
                            if str('checking') == trg_type:
                                trg_data = i
                            else:
                                src_data = i

                    if src_data is not None and trg_data is not None:
                        if src_data['balance'] > amount:
                            src_balance = src_data['balance'] - amount
                            trg_balance = trg_data['balance'] + amount
                            response = dynamodb.transactionUpdate(
                                src_data, trg_data, src_balance, trg_balance, amount)
                            flash(
                                f"{amount} Amount updated into account: {src_data['acc_id']} successfully.", 'success')
                            flash(
                                f"{amount} Amount updated into account:  {trg_data['acc_id']} successfully.", 'success')
                            flash(
                                f"Amount transferred to {trg_data['acc_id']} from {src_data['acc_id']} successfully", 'success')
                        else:
                            flash("Insufficient amount to transfer.", "danger")
                    else:
                        flash("Accounts not found", "danger")
                else:
                    flash("Can't Transfer amount to same account.", 'warning')
            else:
                data = dynamodb.getAccountDetailsByCustId(cust_id)
                if data and len(data) == 2:
                    return render_template('transfer.html', deposit=True, cust_id=cust_id)
                else:
                    flash("Data Not found or Invalid Customer ID", 'danger')
                    return redirect(url_for('viewaccount'))

    return redirect(url_for('viewaccount'))


# code for view account statement based on the account id
# Using number of last transaction
@app.route("/statement", methods=["GET", "POST"])
def statement():
    if 'token' not in session:
        return redirect(url_for('login'))
    if session['usert'] == "customer":
        if request.method == "POST":
            acc_id = request.form.get("acc_id")
            number = request.form.get("number")
            flag = request.form.get("Radio")
            if flag == "red":
                data = dynamodb.getTransactions(int(acc_id), number)
            if data:
                print(data)
                return render_template('statement.html', statement=True, data=data['Items'], acc_id=acc_id)
            else:
                flash("No Transactions", 'danger')
                return redirect(url_for('dashboard'))
    else:
        flash("You don't have access to this page", "warning")
        return redirect(url_for('dashboard'))
    return render_template('statement.html', statement=True)

# code for generating cloudfront urls
@app.route('/investmentresearch',  methods=["GET", "POST"])
def investmentresearch():
    expire_date = dt.datetime(2022, 1, 1)
    if 'token' not in session:
       return redirect(url_for('login'))     
    if session['usert']=='customer':
        #conn = client('s3',
         #   region_name='us-east-1')
        #keyData = conn.list_objects(Bucket=BUCKET_NAME)['Contents']
        conn = client('s3', region_name='us-east-1')
        keyData = conn.list_objects_v2(Bucket=BUCKET_NAME, Prefix='reports')['Contents']
        data = []
        if keyData:
            for key in keyData:
                url = CLOUDFRONT_URL
                name=key['Key']
                if name=='reports/':
                    print(name)
                else:
                    cfUrl = cf.cloudfront_signer.generate_presigned_url(url+'/'+key['Key'], date_less_than=expire_date)
                    keyVal = {"name" :name, "url": cfUrl}
                    data.append(keyVal)
            print(data)
            return render_template('investmentresearch.html', investmentresearch=True, data=data)
        else:
            flash("No files", 'danger')
            return redirect(url_for('dashboard'))
    else:
        flash("You don't have access to this page","warning")
        return redirect(url_for('dashboard'))


@app.route('/')
def sign_in():
    print(aws_auth.get_sign_in_url())
    return redirect(aws_auth.get_sign_in_url())


# route for 404 error
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

# Logout


@app.route("/logout")
def logout():
    session.pop('token', None)
    return redirect(aws_auth.get_sign_in_url())


# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    access_token = aws_auth.get_access_token(request.args)
    if access_token is not None:
        session['token'] = access_token
        session['usert'] = 'customer'
        print(session['token'], session['usert'])
        return redirect(url_for("dashboard"))
    else:
        print("no access token")
    return render_template("login.html", login=True)


# Main
if __name__ == '__main__':

    app.debug = False  
    app.run(host='0.0.0.0',ssl_context='adhoc', port=5000)