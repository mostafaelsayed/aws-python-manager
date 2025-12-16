import boto3
import yaml
import logging
account_directory = 'config/my_account'

class DefaultClient:
    def __init__(self):
        self.sess = boto3.Session(profile_name='aws-python-manager')
    def get_instance(self, service_name):
        return self.sess.client(service_name)
    def get_env(self):
        env = None
        with open(account_directory + '/env.yaml', 'r') as file:
            try:
                env = yaml.safe_load(file)
            except FileNotFoundError as e:
                logging.error("error loading env: ", e)
        return env