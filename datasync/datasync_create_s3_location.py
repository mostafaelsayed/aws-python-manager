from clients.default_client import DefaultClient
from utils.file_utils import parse
client = DefaultClient()
instance = client.get_instance('datasync')
config = parse('datasync/location_configs/s3.yaml')
s3_bucket_name = config['bucket_name']
response = instance.create_location_s3(
    S3BucketArn='arn:aws:s3:::' + s3_bucket_name,
    S3Config={
        'BucketAccessRoleArn': 'arn:aws:iam::508981873847:role/service-role/' + config['bucket_access_role_name'],
    }
)

print(response)