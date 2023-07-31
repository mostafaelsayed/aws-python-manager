import boto3
import utils.file_utils as file_utils

available_services = boto3._get_default_session().get_available_services()

file_utils.write_json(available_services, 'output/available-services.json')