from clients.default_client import DefaultClient
import json

ec2 = DefaultClient().get_instance('ec2')
vpc_ids_to_delete = []
with open('output/vpcs.json', 'r') as file:
    vpcs = json.loads(file.read())
    for vpc in vpcs['Vpcs']:
        if not vpc['IsDefault']:
            vpc_ids_to_delete.append(vpc['VpcId'])

for vpc_id in vpc_ids_to_delete:
    ec2.delete_vpc(VpcId=vpc_id)
    print('vpc with id "' + vpc_id + '" is deleted')