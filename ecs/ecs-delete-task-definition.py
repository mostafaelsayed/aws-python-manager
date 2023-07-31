from clients.default_client import DefaultClient

client = DefaultClient().get_instance('ecs')

response = client.deregister_task_definition(
    taskDefinition='freelancer-backend:8'
)

response1 = client.delete_task_definitions(
    taskDefinitions=[
        'freelancer-backend:8',
    ]
)

print(response)