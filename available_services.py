import utils.file_utils as file_utils

from clients.default_client import DefaultClient

available_services = DefaultClient().get_session().get_available_services()

file_utils.write_json(available_services, 'output/available-services.json')