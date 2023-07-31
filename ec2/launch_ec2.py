from clients.default_client import DefaultClient

client = DefaultClient()
ec2 = client.get_instance('ec2')
env = client.get_env()

print(ec2.run_instances(ImageId=env['ec2_launch_ami'], InstanceType='t2.micro', MinCount=1, MaxCount=1))