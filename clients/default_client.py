import boto3

class DefaultClient:
    def __init__(self):
        self.sess = boto3.Session(profile_name='oidc')
    def get_instance(self, service_name):
        return self.sess.client(service_name)