from clients.default_client import DefaultClient

client = DefaultClient()
instance = client.get_instance('logs')
env = client.get_env()

for log_group in env['ecs_log_groups']:
    try:
        response = instance.delete_log_group(
            logGroupName=log_group
        )
        print('success delete log_group: ' + log_group + ' response : ', response)
    except Exception as e:
        if e.__class__.__name__ == "ResourceNotFoundException":
            print('log_group "' + log_group + '" not found. skipping')