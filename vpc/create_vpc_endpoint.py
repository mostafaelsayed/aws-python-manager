from clients.default_client import DefaultClient

client = DefaultClient()
instance = client.get_instance('ec2')

endpoints = [
    {
        'service_name': 'com.amazonaws.eu-west-1.ecr.api',
        'name': 'ecr-api-endpoint'
    },
    {
        'service_name': 'com.amazonaws.eu-west-1.ecr.dkr',
        'name': 'ecr-dkr-endpoint'
    },
    {
        'service_name': 'com.amazonaws.eu-west-1.ecs',
        'name': 'ecs-endpoint'
    },
    {
        'service_name': 'com.amazonaws.eu-west-1.ecs-agent',
        'name': 'ecs-agent-endpoint'
    },
    {
        'service_name': 'com.amazonaws.eu-west-1.ecs-telemetry',
        'name': 'ecs-telemetry-endpoint'
    }
]
for endpoint in endpoints:
    response = instance.create_vpc_endpoint(
        DryRun=False,
        VpcEndpointType='Interface',
        VpcId='vpc-0268b786efee82004',
        ServiceName=endpoint['service_name'],
        # PolicyDocument='string',
        # RouteTableIds=[
        #     'string',
        # ],
        SubnetIds=[
            'subnet-09f4e2c056b9cfb50',
        ],
        SecurityGroupIds=[
            'sg-04c778d175541256a',
        ],
        IpAddressType='ipv4',
        DnsOptions={
            'DnsRecordIpType': 'ipv4'
        },
        PrivateDnsEnabled=True,
        TagSpecifications=[
            {
                'ResourceType': 'vpc-endpoint',
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
    )

    print(response)