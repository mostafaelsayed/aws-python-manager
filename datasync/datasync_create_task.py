from clients.default_client import DefaultClient
from datasync.datasync_task_waiter import create_datasync_task_waiter

def create_task(source_location_id, destination_location_id):
    client = DefaultClient()
    env = client.get_env()
    instance = client.get_instance('datasync')
    response = instance.create_task(
        SourceLocationArn='arn:aws:datasync:{0}:{1}:location/{2}'.format(client.region, env['aws_account_id'], source_location_id),
        DestinationLocationArn='arn:aws:datasync:{0}:{1}:location/{2}'.format(client.region, env['aws_account_id'], destination_location_id),
    )
    if response['TaskArn'] != None:
        print('DataSync task with ARN: {0} has been created successfully'.format(response['TaskArn']))
        create_datasync_task_waiter('AVAILABLE').wait(TaskArn=response['TaskArn'])
        print('Task with ARN: {0} has been created successfully'.format(response['TaskArn']))
    else:
        print('Failed to create DataSync task: ', response)
        raise('Failed to create DataSync task')

    return response