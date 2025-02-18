from clients.default_client import DefaultClient

client = DefaultClient().get_instance('ecs')
cluster = 'dev'
family = 'mysql-organizer'
tasks_response = client.list_tasks(
    cluster=cluster,
    family=family
)
print(tasks_response)
for task_arn in tasks_response['taskArns']:
    response = client.stop_task(
        cluster=cluster,
        task=task_arn
    )

    print(response)