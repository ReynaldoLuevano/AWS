from aws_cdk import (
    Stack,
    aws_s3 as s3
)
from constructs import Construct

class Application1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # Ensure bucket uniqueness
        bucket_name = "jumpingbrainsops203cx"

        # Create the S3 bucket
        ops203_bucket = s3.Bucket(
            self,
            "myBucket",
            bucket_name=bucket_name,
            versioned=False
        )
        
