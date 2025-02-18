from clients.default_client import DefaultClient

client = DefaultClient()
env = client.get_env()
instance = client.get_instance('datasync')
source_location_arn = 'loc-04cc471df1a5a32cf'
destination_location_arn = 'loc-0b050b7d974e9486b'
response = instance.create_task(
    SourceLocationArn='arn:aws:datasync:{0}:{1}:location/{2}'.format(client.get_region(), env['aws_account_id'], source_location_arn),
    DestinationLocationArn='arn:aws:datasync:{0}:{1}:location/{2}'.format(client.get_region(), env['aws_account_id'], destination_location_arn),
)
print(response)