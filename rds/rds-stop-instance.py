from clients.default_client import DefaultClient

client = DefaultClient().get_instance('rds')

response = client.stop_db_instance(
    DBInstanceIdentifier='database-1'
)

print(response)