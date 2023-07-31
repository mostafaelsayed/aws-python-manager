from config.config import load_default
import boto3

class DefaultClient:
    def __init__(self) -> None:
        self.credentials, self.region_value, self.env = load_default()

    def get_credentials(self):
        return self.credentials
    
    def get_region(self):
        return self.region_value
    
    def get_env(self):
        return self.env

    def get_instance(self, service_name):
        return boto3.client(service_name, region_name=self.region_value,
                            aws_access_key_id=self.credentials['aws_access_key_id'],
                            aws_secret_access_key=self.credentials['aws_secret_access_key'])