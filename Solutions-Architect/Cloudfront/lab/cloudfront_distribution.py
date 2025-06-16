import datetime
from botocore.exceptions import ClientError
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from botocore.signers import CloudFrontSigner
import rsa, configparser

config = configparser.ConfigParser()
config.read(r'config.txt')


key_id=config.get('PARAMS_DETAILS','AWS_KEY_ID')
url=config.get('PARAMS_DETAILS', 'AWS_CLOUDFRONT_URL')
pem_file=config.get('PARAMS_DETAILS', 'AWS_PEM_FILE')


def rsa_signer(message):
    private_key = open(pem_file, 'r').read()
    return rsa.sign(message, rsa.PrivateKey.load_pkcs1(private_key.encode('utf8')),'SHA-1')

expire_date = datetime.datetime(2026, 1, 1)

cloudfront_signer = CloudFrontSigner(key_id, rsa_signer)

# Create a signed url that will be valid until the specific expiry date
# provided using a canned policy.
signed_url = cloudfront_signer.generate_presigned_url(
    url, date_less_than=expire_date)
print(signed_url)