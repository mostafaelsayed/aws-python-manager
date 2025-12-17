from clients.default_client import DefaultClient

client = DefaultClient()
instance = client.get_instance('ecs')
response = instance.create_cluster(
    clusterName='dev'
)

print(response)