import json
import yaml

def write_json(response, file_name):
    with open(file_name, 'w') as file:
        file.write(json.dumps(response, indent=4, default=str))

def parse(file_name):
    with open(file_name, 'r') as file:
        try:
            response = yaml.safe_load(file)
            return response
        except FileNotFoundError as e:
            print('cannot parse file with name: ' + file_name + '. exception details: ', e)