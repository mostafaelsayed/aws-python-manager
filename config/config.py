import yaml
import os

def load_default_env_from_env_vars():
    env = {}
    env['ecr_image_url'] = os.getenv('ecr_image_url')
    env['ec2_launch_ami'] = os.getenv('ec2_launch_ami')
    env['ec2_launch_instance_type'] = os.getenv('ec2_launch_instance_type')
    env['ecs_fargate_security_groups'] = os.getenv('ecs_fargate_security_groups')
    env['ecs_fargate_subnets'] = os.getenv('ecs_fargate_subnets')

    return env

def load_default():
    credentials = {}
    env = {}
    region_key = ''
    region_value = ''
    account_directory = 'config/my_account'
    with open(account_directory + '/credentials.yaml', 'r') as file:
        try:
            credentials = yaml.safe_load(file)
        except FileNotFoundError:
            credentials['aws_access_key_id'] = os.getenv('aws_access_key_id')
            credentials['aws_secret_access_key'] = os.getenv('aws_secret_access_key')
    with open(account_directory + '/env.yaml', 'r') as file:
        try:
            env = yaml.safe_load(file)
            region_key = env['region']
        except FileNotFoundError:
            env = load_default_env_from_env_vars()
            region_key = env['region']
    with open('regions.yaml', 'r') as file:
        try:
            regions = yaml.safe_load(file)
            region_value = regions[region_key]
        except FileNotFoundError:
            region_value = os.getenv('aws_default_region')

    return credentials, region_value, env