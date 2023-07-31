from clients.default_client import DefaultClient
import utils.file_utils as file_utils

client = DefaultClient()

account = client.get_instance('account')
sts = client.get_instance('sts')

file_utils.write_json(account.get_contact_information(), 'output/account-contact-info.json')
file_utils.write_json(sts.get_caller_identity(), 'output/account-info.json')