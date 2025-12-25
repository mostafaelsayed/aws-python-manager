from clients.default_client import DefaultClient
from utils.file_utils import parse
client = DefaultClient()
instance = client.get_instance('elbv2')
configs = parse('ec2/elb/current.yaml')

import traceback

for config in configs:
    try:
        response = instance.create_load_balancer(
            Name=config['name'],
            Subnets=config['subnet_ids'],
            # SubnetMappings=[
            #     {
            #         'SubnetId': 'string',
            #         'AllocationId': 'string',
            #         'PrivateIPv4Address': 'string',
            #         'IPv6Address': 'string',
            #         'SourceNatIpv6Prefix': 'string'
            #     },
            # ],
            SecurityGroups=config['security_groups'],
            Scheme='internal',
            Tags=[
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            Type='application',
            IpAddressType=config['ip_address_type'],
            # CustomerOwnedIpv4Pool='string',
            # EnablePrefixForIpv6SourceNat='on'|'off',
            # IpamPools={
            #     'Ipv4IpamPoolId': 'string'
            # }
        )

        print(response)

        load_balancer_arn = response['LoadBalancers'][0]['LoadBalancerArn']

        # response_2 = instance.create_target_group(
        #     Name=config['target_group']['name'],
        #     Protocol=config['target_group']['protocol'],
        #     # ProtocolVersion='string',
        #     Port=config['target_group']['port'],
        #     VpcId=config['target_group']['vpc_id'],
        #     # HealthCheckProtocol='HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP'|'GENEVE'|'QUIC'|'TCP_QUIC',
        #     # HealthCheckPort='string',
        #     # HealthCheckEnabled=True|False,
        #     # HealthCheckPath='string',
        #     # HealthCheckIntervalSeconds=123,
        #     # HealthCheckTimeoutSeconds=123,
        #     # HealthyThresholdCount=123,
        #     # UnhealthyThresholdCount=123,
        #     # Matcher={
        #     #     'HttpCode': 'string',
        #     #     'GrpcCode': 'string'
        #     # },
        #     TargetType=config['target_group']['target_type'],
        #     Tags=config['target_group']['tags'],
        #     IpAddressType=config['target_group']['ip_address_type']
        #     # TargetControlPort=123
        # )

        # print(response_2)

        # target_group_arn = response_2['TargetGroups'][0]['TargetGroupArn']

        # response = instance.modify_target_group_attributes(
        #     TargetGroupArn=target_group_arn,
        #     Attributes=[
        #         {
        #             'Key': 'deregistration_delay.timeout_seconds',
        #             'Value': '5'
        #         },
        #     ]
        # )

        # print(response)

        default_actions = config['listener']['default_actions']
        default_actions[0]['TargetGroupArn'] = 'arn:aws:elasticloadbalancing:eu-west-1:508981873847:targetgroup/organizer-backend-target-group/96fa2143afad97b2'
        response_3 = instance.create_listener(
            LoadBalancerArn=load_balancer_arn,
            Protocol=config['listener']['protocol'],
            Port=config['listener']['port'],
            # SslPolicy='string',
            # Certificates=[
            #     {
            #         'CertificateArn': config['listener']['certificate_arn']
            #     },
            # ],
            
            DefaultActions=default_actions,
        )

        print(response_3)
    except Exception as e:
        print(traceback.print_tb(e.__traceback__))