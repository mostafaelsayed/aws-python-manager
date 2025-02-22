from clients.default_client import DefaultClient
import efs.efs_utils as efs_utils

def create_efs_location(efs_location_config):
    client = DefaultClient()
    env = client.get_env()
    instance = client.get_instance('datasync')
    file_system_name = efs_location_config['file_system_name']
    file_system_id = efs_utils.get_file_system_id_by_name(file_system_name)
    security_groups_arns = []
    security_groups = efs_location_config['ec2_config']['security_groups']
    for security_group in security_groups:
        security_groups_arns.append('arn:aws:ec2:{0}:{1}:security-group/{2}'.format(client.get_region(), env['aws_account_id'], security_group))
    
    response = instance.create_location_efs(
        Ec2Config={
            'SubnetArn': 'arn:aws:ec2:{0}:{1}:subnet/{2}'.format(client.get_region(), env['aws_account_id'], efs_location_config['ec2_config']['subnet']),
            'SecurityGroupArns': security_groups_arns,
        },
        EfsFilesystemArn='arn:aws:elasticfilesystem:{0}:{1}:file-system/{2}'.format(client.get_region(), env['aws_account_id'], file_system_id),
    )

    if response['LocationArn'] != None:
        print('efs Location with ARN: {0} has been created successfully'.format(response['LocationArn']))
    else:
        print('Failed to create efs Location: ', response)
        raise('Failed to create efs Location')

    return response