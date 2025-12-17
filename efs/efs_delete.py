from clients.default_client import DefaultClient
from utils.file_utils import parse
import efs_utils
from efs_delete_mount_target import delete_mount_target
from efs_waiter import create_efs_waiter
from botocore.exceptions import WaiterError

def delete_efs():
    client = DefaultClient()
    config = parse('efs/config.yaml')
    efs_instance = client.get_instance('efs')
    for element in config:
        file_system_name = element['file_system_name']
        delete_mount_target(element)
        try:
            file_system_id = efs_utils.get_file_system_id_by_name(file_system_name)
            response = efs_instance.delete_file_system(FileSystemId=file_system_id)
            if response['ResponseMetadata']['HTTPStatusCode'] == 204:
                print('Deleting file system with id: ', file_system_id)
            create_efs_waiter(efs_instance, 'deleted').wait(FileSystemId=file_system_id)
            print('File system {0} with id {1} has been deleted successfully'.format(file_system_name, file_system_id))
        except WaiterError as e:
            last_response = e.last_response
            if last_response['Error']['Code'] == 'FileSystemNotFound':
                print('File system {0} with id {1} has been deleted successfully'.format(file_system_name, file_system_id))
            else:
                print('unexpected efs delete waiter error {0}: {1}'.format(last_response['Error']['Code'], last_response['Error']['Message']))
        except Exception as e:
            print('Error: ', e)
            return

delete_efs()