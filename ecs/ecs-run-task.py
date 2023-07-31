from clients.default_client import DefaultClient

client = DefaultClient()
credentials = client.get_credentials()
env = client.get_env()
instance = client.get_instance('ecs')
cluster = 'dev'
task_definition = 'freelancer-backend'
response = instance.run_task(
    cluster=cluster,
    count=1,
    enableECSManagedTags=False,
    enableExecuteCommand=False,
    launchType='FARGATE',
    networkConfiguration={
        'awsvpcConfiguration': {
            'subnets': env['ecs_fargate_subnets'],
            'securityGroups': env['ecs_fargate_security_groups'],
            'assignPublicIp': 'ENABLED'
        }
    },
    tags=[
        {
            'key': 'app',
            'value': 'freelancer'
        },
    ],
    taskDefinition=task_definition
)

print(response)