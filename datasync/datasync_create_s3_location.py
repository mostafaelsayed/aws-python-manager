from clients.default_client import DefaultClient

def create_s3_location(s3_location_config):
    client = DefaultClient()
    env = client.get_env()
    instance = client.get_instance('datasync')
    s3_bucket_name = s3_location_config['bucket_name']
    response = instance.create_location_s3(
        S3BucketArn='arn:aws:s3:::' + s3_bucket_name,
        S3Config={
            'BucketAccessRoleArn': 'arn:aws:iam::{0}:role/{1}'.format(env['aws_account_id'], s3_location_config['bucket_access_role_name']),
        }
    )

    if response['LocationArn'] != None:
        print('S3 Location with ARN: {0} has been created successfully'.format(response['LocationArn']))
    else:
        print('Failed to create S3 Location: ', response)
        raise('Failed to create S3 Location')
    return response