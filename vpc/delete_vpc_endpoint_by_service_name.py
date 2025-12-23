from clients.default_client import DefaultClient
from utils.file_utils import parse

def delete_vpc_endpoints():
    client = DefaultClient()
    vpc_endpoint_ids = []
    instance = client.get_instance('ec2')
    endpoints = parse('vpc/vpc-endpoint-configs/vpc_endpoint_config.yaml')
    service_names = []
    for endpoint in endpoints:
        service_names.append(endpoint['service_name'])
    endpoints_response = instance.describe_vpc_endpoints(
        Filters=[
            {
                'Name': 'service-name',
                'Values': service_names
            }
        ]
    )

    for endpoint in endpoints_response['VpcEndpoints']:
        vpc_endpoint_ids.append(endpoint['VpcEndpointId'])
    response = instance.delete_vpc_endpoints(VpcEndpointIds=vpc_endpoint_ids)
    print(response)

delete_vpc_endpoints()