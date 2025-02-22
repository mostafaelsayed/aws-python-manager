from clients.default_client import DefaultClient
from mount_target_waiter import create_mount_target_waiter

def create_mount_target(config, file_system_id):
    client = DefaultClient()
    instance = client.get_instance('efs')
    response = instance.create_mount_target(
        FileSystemId=file_system_id,
        SubnetId=config['mount_target']['subnet_id'],
        SecurityGroups=config['mount_target']['security_groups']
    )
    mount_target_id = response['MountTargetId']
    if mount_target_id != None:
        print('creating mount target with id: ', mount_target_id)
    create_mount_target_waiter(instance, 'available').wait(MountTargetId=mount_target_id)
    print('Mount target created successfully')