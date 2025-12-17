from clients.default_client import DefaultClient

client = DefaultClient()

ecr = client.get_instance('ecr')
env = client.get_env()

response = ecr.delete_repository(
    registryId=env['aws_account_id'],
    repositoryName=env['ecr_repository_name']
)

print(response)