import datetime

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from botocore.signers import CloudFrontSigner


key_id = 'KW1EEAQR9Q5PB'
url = 'https://d1babeuz3o5ez4.cloudfront.net/dino1.jpg'
expire_date = datetime.datetime(2025, 12, 1)


def rsa_signer(message):
    with open('private_key.pem', 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key.sign(message, padding.PKCS1v15(), hashes.SHA1())


cloudfront_signer = CloudFrontSigner(key_id, rsa_signer)

# Create a signed url that will be valid until the specific expiry date
# provided using a canned policy.
signed_url = cloudfront_signer.generate_presigned_url(
    url, date_less_than=expire_date)
print(signed_url)