#create an s3 bucket using boto3
import boto3

client = boto3.client('s3')

response = client.create_bucket(
    ACL='private',
    Bucket='galicia123123123123',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-south-2'
    },
)

print(response)

