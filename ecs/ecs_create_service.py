from clients.default_client import DefaultClient
from utils.file_utils import parse
from utils.common_utils import attach_ecs_service_connect_services
client = DefaultClient()
instance = client.get_instance('ecs')
references = parse('ecs/task-configuration/current.yaml')['task_references']
for reference in references:
    try:
        service_config = parse('ecs/service-configuration/{0}/service_config.yaml'.format(reference))
        response = instance.create_service(
            cluster=service_config['cluster'],
            serviceName=service_config['service_name'],
            taskDefinition=service_config['task_definition'],
            desiredCount=service_config['desired_count'],
            launchType=service_config['launch_type'],
            networkConfiguration={
                'awsvpcConfiguration': {
                    'subnets': service_config['subnet_ids'],
                    'securityGroups': service_config['security_groups'],
                    'assignPublicIp': service_config['assign_public_ip']
                }
            },
            schedulingStrategy=service_config['scheduling_strategy'],
            deploymentController={
                'type': service_config['deployment_controller_type']
            },
            tags=service_config['tags'],
            serviceConnectConfiguration={
                'enabled': service_config['service_connect_configuration']['enabled'],
                'namespace': service_config['service_connect_configuration']['namespace'],
                'services': attach_ecs_service_connect_services(service_config['service_connect_configuration']),
            },
        )

        print(response)
    except Exception as e:
        print('error')