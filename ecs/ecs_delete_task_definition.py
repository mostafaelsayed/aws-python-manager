from clients.default_client import DefaultClient

client = DefaultClient()
ecs = client.get_instance('ecs')
env = client.get_env()
task_definition_name = 'mysql-organizer'
task_definition = ecs.describe_task_definition(
    taskDefinition=task_definition_name
)
taskDefinitionRevision = task_definition['taskDefinition']['revision']
response = ecs.deregister_task_definition(
    taskDefinition=task_definition_name + ':' + str(taskDefinitionRevision)
)

response1 = ecs.delete_task_definitions(
    taskDefinitions=[
        task_definition_name + ':' + str(taskDefinitionRevision)
    ]
)

print(response)