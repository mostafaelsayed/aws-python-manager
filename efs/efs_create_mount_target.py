from clients.default_client import DefaultClient
from mount_target_waiter import create_mount_target_waiter

def attach_security_groups(config):
    if 'security_groups' in config['mount_target']:
        return config['mount_target']['security_groups']
    return []

def create_mount_target(config, file_system_id):
    client = DefaultClient()
    instance = client.get_instance('efs')
    response = instance.create_mount_target(
        FileSystemId=file_system_id,
        SubnetId=config['mount_target']['subnet_id'],
        SecurityGroups=attach_security_groups(config)
    )
    mount_target_id = response['MountTargetId']
    if mount_target_id != None:
        print('creating mount target with id: ', mount_target_id)
    create_mount_target_waiter(instance, 'available').wait(MountTargetId=mount_target_id)
    print('Mount target created successfully')