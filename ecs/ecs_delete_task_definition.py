from clients.default_client import DefaultClient
from utils.file_utils import parse
client = DefaultClient()
ecs = client.get_instance('ecs')
references = parse('ecs/task-configuration/current.yaml')['task_references']
for reference in references:
    try:   
        config = parse('ecs/task-configuration/{0}/task-definition.yaml'.format(reference))
        task_definition_name = config['family']
        task_definition = ecs.describe_task_definition(
            taskDefinition=task_definition_name
        )
        taskDefinitionRevision = task_definition['taskDefinition']['revision']
        response = ecs.deregister_task_definition(
            taskDefinition=task_definition_name + ':' + str(taskDefinitionRevision)
        )
    
        response1 = ecs.delete_task_definitions(
            taskDefinitions=[
                task_definition_name + ':' + str(taskDefinitionRevision)
            ]
        )

        print(response)
    except Exception as e:
        print('error')

    