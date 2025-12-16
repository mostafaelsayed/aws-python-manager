from clients.default_client import DefaultClient

client = DefaultClient()

ecr = client.get_instance('ecr')
env = client.get_env()

response = ecr.create_repository(
    registryId=env['aws_account_id'],
    repositoryName=env['ecr_repository_name'],
    tags=[
        {
            'Key': 'app',
            'Value': 'organizer'
        },
    ],
    imageTagMutability='MUTABLE', # 'MUTABLE'|'IMMUTABLE'
    imageScanningConfiguration={
        'scanOnPush': False
    },
    encryptionConfiguration={
        'encryptionType': 'AES256'
    }
)
print(response)