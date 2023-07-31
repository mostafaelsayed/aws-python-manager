from clients.default_client import DefaultClient
import utils.file_utils as file_utils

ec2 = DefaultClient().get_instance('ec2')

list = ec2.describe_instances()
active_list = {'Reservations': []}
active_instances = []
for reservation in list['Reservations']:
    active_instances = []
    for instance in reservation['Instances']:
        if instance['State']['Name'] != 'terminated' and instance['State']['Name'] != 'shutting-down':
            active_instances.append(instance)
    if len(active_instances) != 0:
        reservation['Instances'] = active_instances
        active_list['Reservations'].append(reservation)
file_utils.write_json(active_list, 'output/ec2-active-instances.json')