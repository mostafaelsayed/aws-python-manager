from clients.default_client import DefaultClient
from utils.file_utils import parse
from efs_create_mount_target import create_mount_target
from efs.efs_waiter import create_efs_waiter

def create_efs_with_mount_target():
    client = DefaultClient()
    instance = client.get_instance('efs')
    config = parse('efs/config.yaml')
    for element in config:
        file_system_name = element['file_system_name']
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
        file_system_id = response['FileSystemId']
        if file_system_id != None:
            print('creating file system with id: ', file_system_id)
        else:
            print('Failed to create file system: ', response)
            return
        create_efs_waiter(instance, 'available').wait(FileSystemId=file_system_id)
        print('File system created successfully with id: ', file_system_id)
        create_mount_target(
            config=element,
            file_system_id=file_system_id
        )

create_efs_with_mount_target()