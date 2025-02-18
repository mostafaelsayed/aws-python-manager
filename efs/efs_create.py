from clients.default_client import DefaultClient
from utils.file_utils import parse

client = DefaultClient()
instance = client.get_instance('efs')
current = parse('efs/configuration/current.yaml')
reference = current['file_system_reference']
config = parse('efs/configuration/{0}.yaml'.format(reference))
file_system_name = config['file_system_name']
response = instance.create_file_system(
    Encrypted=True,
    Tags=[
        {
            'Key': 'Name',
            'Value': file_system_name
        },
        {
            'Key': 'file-system-name',
            'Value': file_system_name
        }
    ]
)

print(response)