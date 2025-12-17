from clients.default_client import DefaultClient
from utils.file_utils import parse

client = DefaultClient().get_instance('ecs')
cluster = 'dev'
reference = parse('ecs/task-configuration/current.yaml')['task_reference']
config = parse('ecs/task-configuration/{0}/task-definition.yaml'.format(reference))
family = config['family']
tasks_response = client.list_tasks(
    cluster=cluster,
    family=family
)
print(tasks_response)
for task_arn in tasks_response['taskArns']:
    response = client.stop_task(
        cluster=cluster,
        task=task_arn
    )

    print(response)