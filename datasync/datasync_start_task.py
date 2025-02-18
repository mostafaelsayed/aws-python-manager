from clients.default_client import DefaultClient

client = DefaultClient()
env = client.get_env()
instance = client.get_instance('datasync')
task_id = 'task-07e026f91d73dcfb6'
response = instance.start_task_execution(
    TaskArn='arn:aws:datasync:{0}:{1}:task/{2}'.format(client.get_region(), env['aws_account_id'], task_id),
)
print(response)