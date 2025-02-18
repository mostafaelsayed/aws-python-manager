from clients.default_client import DefaultClient
from utils.file_utils import parse
import efs.efs_utils as efs_utils

client = DefaultClient()
env = client.get_env()
instance = client.get_instance('datasync')
config = parse('datasync/location_configs/efs.yaml')
file_system_name = config['file_system_name']
file_system_id = efs_utils.get_file_system_id_by_name(file_system_name)
security_groups_arns = []
security_groups = config['ec2_config']['security_groups']
for security_group in security_groups:
    security_groups_arns.append('arn:aws:ec2:{0}:{1}:security-group/{2}'.format(client.get_region(), env['aws_account_id'], security_group))
response = instance.create_location_efs(
    Ec2Config={
        'SubnetArn': 'arn:aws:ec2:{0}:{1}:subnet/{2}'.format(client.get_region(), env['aws_account_id'], config['ec2_config']['subnet']),
        'SecurityGroupArns': security_groups_arns,
    },
    EfsFilesystemArn='arn:aws:elasticfilesystem:{0}:{1}:file-system/{2}'.format(client.get_region(), env['aws_account_id'], file_system_id),
)

print(response)