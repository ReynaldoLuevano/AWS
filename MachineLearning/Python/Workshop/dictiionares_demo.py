
#creating a dictionary
account_details={}
user_details =  dict()

#adding an item
account_details['first_name'] = 'Jhon'
user_details['last_name'] = 'Doe'

print(account_details)
print(user_details)

#modifying an item
account_details['first_name'] = 'Juan'
user_details['last_name'] = 'Martinez'

print(account_details)
print(user_details)

#deleting an item
del user_details['last_name']
print(user_details)