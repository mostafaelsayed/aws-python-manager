from clients.default_client import DefaultClient
from utils.file_utils import parse
client = DefaultClient()
instance = client.get_instance('elbv2')
configs = parse('ec2/elb/current.yaml')

import traceback

for config in configs:
    try:
        alb_arn = instance.describe_load_balancers(Names=[config['name']])['LoadBalancers'][0]['LoadBalancerArn']
        listener_arn = instance.describe_listeners(LoadBalancerArn=alb_arn)['Listeners'][0]['ListenerArn']

        response = instance.delete_listener(ListenerArn=listener_arn)
        print(response)

        response = instance.delete_load_balancer(
            LoadBalancerArn=alb_arn
        )

        print(response)

        
        
        arn = instance.describe_target_groups(Names=[config['target_group']['name']])['TargetGroups'][0]['TargetGroupArn']
        response = instance.delete_target_group(
            TargetGroupArn=arn
        )

        print(response)
    except Exception as e:
        print(traceback.print_tb(e.__traceback__))