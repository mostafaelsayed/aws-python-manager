from clients.default_client import DefaultClient
from utils.file_utils import parse
import efs_utils

client = DefaultClient()
instance = client.get_instance('efs')
current = parse('efs/configuration/current.yaml')
reference = current['file_system_reference']
config = parse('efs/configuration/{0}.yaml'.format(reference))
file_system_name = config['file_system_name']
response = instance.delete_mount_target(
    MountTargetId=efs_utils.get_mount_target_id_by_file_system_name(file_system_name)
)
print(response)