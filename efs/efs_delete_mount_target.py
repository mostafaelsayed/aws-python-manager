from clients.default_client import DefaultClient
import efs_utils
from mount_target_waiter import create_mount_target_waiter
from botocore.exceptions import WaiterError

def delete_mount_target(config):
    client = DefaultClient()
    instance = client.get_instance('efs')
    file_system_name = config['file_system_name']
    mount_target_id = efs_utils.get_mount_target_id_by_file_system_name(file_system_name)
    response = instance.delete_mount_target(
        MountTargetId=mount_target_id
    )
    if response['ResponseMetadata']['HTTPStatusCode'] == 204:
        print('Deleting mount target for file system {0} with id {1}: '.format(file_system_name, mount_target_id))
    try:
        create_mount_target_waiter(instance, 'deleted').wait(MountTargetId=mount_target_id)
        print('Mount Target for file system {0} with id {1} has been deleted successfully'.format(file_system_name, mount_target_id))
    except WaiterError as e:
        last_response = e.last_response
        if last_response['Error']['Code'] == 'MountTargetNotFound':
            print('Mount Target for file system {0} with id {1} has been deleted successfully'.format(file_system_name, mount_target_id))
        else:
            print('unexpected efs delete mount target waiter error {0}: {1}'.format(last_response['Error']['Code'], last_response['Error']['Message']))
    except Exception as e:
        print('Error: ', e)
        return