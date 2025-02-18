from clients.default_client import DefaultClient
from utils.file_utils import parse

client = DefaultClient()
instance = client.get_instance('ecs')
reference = parse('ecs/task-configuration/current.yaml')['task_reference']
task_run_configuration = parse('ecs/task-configuration/{0}/run-configuration.yaml'.format(reference))
response = instance.run_task(
    cluster=task_run_configuration['cluster'],
    count=task_run_configuration['count'],
    enableECSManagedTags=task_run_configuration['enableECSManagedTags'],
    enableExecuteCommand=task_run_configuration['enableExecuteCommand'],
    launchType=task_run_configuration['launchType'],
    networkConfiguration=task_run_configuration['networkConfiguration'],
    tags=task_run_configuration['tags'],
    taskDefinition=task_run_configuration['taskDefinition']
)

print(response)