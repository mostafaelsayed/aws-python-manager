from clients.default_client import DefaultClient
from utils.file_utils import parse
import efs.efs_utils as efs_utils
client = DefaultClient()
instance = client.get_instance('ecs')
region_value = client.get_region()
env = client.get_env()
reference = parse('ecs/task-configuration/current.yaml')['task_reference']
task_definition = parse('ecs/task-configuration/{0}/task-definition.yaml'.format(reference))
task_definition_volumes = task_definition['volumes']
volumes = []
for volume in task_definition_volumes:
    efs_name = volume['efsVolumeConfiguration']['fileSystemName']
    file_system_id = efs_utils.get_file_system_id_by_name(efs_name)
    volume['efsVolumeConfiguration']['fileSystemId'] = file_system_id
    del volume['efsVolumeConfiguration']['fileSystemName']
    volumes.append(volume)
response = instance.register_task_definition(
    volumes=volumes,
    containerDefinitions=task_definition['containerDefinitions'],
    cpu=task_definition['cpu'],
    memory=task_definition['memory'],
    family=task_definition['family'],
    runtimePlatform=task_definition['runtimePlatform'],
    taskRoleArn=task_definition['taskRoleArn'],
    executionRoleArn=task_definition['executionRoleArn'],
    tags=task_definition['tags'],
    requiresCompatibilities=task_definition['requiresCompatibilities'],
    networkMode=task_definition['networkMode'],
)

print(response)