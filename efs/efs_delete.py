from clients.default_client import DefaultClient
from utils.file_utils import parse
import efs_utils

client = DefaultClient()
reference = parse('efs/configuration/current.yaml')['file_system_reference']
config = parse('efs/configuration/{0}.yaml'.format(reference))
file_system_name = config['file_system_name']
file_system_id = efs_utils.get_file_system_id_by_name(file_system_name)
print('file_system_id to delete: ', file_system_id)
efs_instance = client.get_instance('efs')
response = efs_instance.delete_file_system(FileSystemId=file_system_id)
print(response)