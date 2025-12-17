from clients.default_client import DefaultClient
import json

instanceIds = []
ec2 = DefaultClient().get_instance('ec2')
with open('output/ec2-active-instances.json', 'r') as file:
    instances = json.loads(file.read())
    instances['Reservations']
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instanceIds.append(instance['InstanceId'])

print(ec2.terminate_instances(InstanceIds=instanceIds))