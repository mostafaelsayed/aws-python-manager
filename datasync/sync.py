from datasync_create_efs_location import create_efs_location
from datasync_create_s3_location import create_s3_location
from datasync_create_task import create_task
from datasync_start_task import start_task
from utils.file_utils import parse


def sync():
    config = parse('datasync/config.yaml')
    for element in config:
        source_location_id = None
        destination_location_id = None
        if element['source']['type'] == 's3':
            source_location_id = create_s3_location(element['source'])['LocationArn'].split('/')[-1]
        if element['destination']['type'] == 'efs':
            destination_location_id = create_efs_location(element['destination'])['LocationArn'].split('/')[-1]
        task_arn = create_task(source_location_id, destination_location_id)['TaskArn']
        start_task(task_arn.split('/')[-1])

sync()