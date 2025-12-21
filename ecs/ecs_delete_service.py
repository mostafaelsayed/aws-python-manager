from clients.default_client import DefaultClient
from utils.file_utils import parse

client = DefaultClient()
instance = client.get_instance('ecs')
references = parse('ecs/task-configuration/current.yaml')['task_references']
for reference in references:
    try:
        service_config = parse('ecs/service-configuration/{0}/service_config.yaml'.format(reference))
        response = instance.delete_service(
            cluster=service_config['cluster'],
            service=service_config['service_name'],
            force=True
        )

        print(response)
    except Exception as e:
        print('error')