from clients.default_client import DefaultClient
import utils.file_utils as file_utils

ec2 = DefaultClient().get_instance('ec2')

list = ec2.describe_vpcs()

file_utils.write_json(list, 'output/vpcs.json')