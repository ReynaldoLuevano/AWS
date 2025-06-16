from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_ec2 as ec2
)
from constructs import Construct

class AppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ###### Network ######

        # Create a VPC
        gxp_vpc = ec2.Vpc(self, "GxP-VPC",
            ip_addresses=ec2.IpAddresses.cidr("10.1.0.0/16"),
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                )
            ]
        )

        ###### Network ######

        ###### Storage ######

        # Ensure bucket uniqueness
        bucket_name = "jumpingbrains156165165165165"

        # Create the S3 bucket
        cloudtrail_bucket = s3.Bucket(
            self,
            "myBucket",
            bucket_name=bucket_name,
            versioned=False
        )