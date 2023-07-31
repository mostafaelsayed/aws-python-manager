from clients.default_client import DefaultClient

client = DefaultClient()
instance = client.get_instance('ecs')
region_value = client.get_region()
env = client.get_env()
response = instance.register_task_definition(
    containerDefinitions=[
        {
            'name': env['ecs_task_definition_container_name'],
            'essential': True,
            'logConfiguration': {
                'logDriver': 'awslogs',
                'options': {
                    'awslogs-region': region_value,
                    'awslogs-group': env['ecs_log_groups'][1],
                    'awslogs-stream-prefix': 'ecs',
                    'awslogs-create-group': 'true'
                }
            },
            'image': client.get_credentials()['ecr_freelancer_backend_image_url'],
        },
    ],
    cpu='256',
    memory='512',
    family='freelancer-backend',
    runtimePlatform={
        'cpuArchitecture': 'X86_64',
        'operatingSystemFamily': 'LINUX'
    },
    executionRoleArn='ecsTaskExecutionRole',
    tags=[
        {
            'key': 'app',
            'value': 'freelancer'
        },
    ],
    requiresCompatibilities=['FARGATE'],
    networkMode='awsvpc'
)

print(response)