from clients.default_client import DefaultClient

def start_task(task_id):
    client = DefaultClient()
    env = client.get_env()
    instance = client.get_instance('datasync')
    response = instance.start_task_execution(
        TaskArn='arn:aws:datasync:{0}:{1}:task/{2}'.format(client.get_region(), env['aws_account_id'], task_id),
    )
    if response['TaskExecutionArn'] != None:
        print('Task with Arn {0} started successfully'.format(response['TaskExecutionArn']))