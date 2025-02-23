from clients.default_client import DefaultClient
from utils.file_utils import parse

def create_vpc_endpoints():
    client = DefaultClient()
    instance = client.get_instance('ec2')
    endpoints = parse('vpc/vpc_endpoint_config.yaml')
    
    for endpoint in endpoints:
        route_table_ids = []
        subnet_ids = []
        security_group_ids = []
        
        args = {
            'DryRun': False,
            'VpcEndpointType': endpoint['type'],
            'VpcId': endpoint['vpc_id'],
            'ServiceName': endpoint['service_name'],
            'TagSpecifications': [
                {
                    'ResourceType': endpoint['resource_type'],
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': endpoint['name']
                        },
                    ]
                },
            ],
                        # SubnetConfigurations=[
            #     {
            #         'SubnetId': 'subnet-09f4e2c056b9cfb50',
            #         'Ipv4': 'string',
            #         'Ipv6': 'string'
            #     },
            # ],
            # ServiceNetworkArn='string',
            # ResourceConfigurationArn='string',
            # ServiceRegion='string'
        }

        if 'route_table_ids' in endpoint:
            for id in endpoint['route_table_ids']:
                route_table_ids.append(id)
            args['RouteTableIds'] = route_table_ids
        if 'subnet_ids' in endpoint:
            for id in endpoint['subnet_ids']:
                subnet_ids.append(id)
            args['SubnetIds'] = subnet_ids
        if 'security_group_ids' in endpoint:
            for id in endpoint['security_group_ids']:
                security_group_ids.append(id)
            args['SecurityGroupIds'] = security_group_ids
        if 'private_dns' in endpoint:
            args['PrivateDnsEnabled'] = endpoint['private_dns']
        if 'ip_address_type' in endpoint:
            args['IpAddressType'] = endpoint['ip_address_type']
        if 'dns' in endpoint:
            dns_record_ip_type = 'ipv4'
            if endpoint['dns'] != None and 'dns_record_ip_type' in endpoint['dns']:
                dns_record_ip_type = endpoint['dns']['dns_record_ip_type']
            args['DnsOptions'] = {
                'DnsRecordIpType': dns_record_ip_type
            }
        response = instance.create_vpc_endpoint(**args)

        print(response)

create_vpc_endpoints()