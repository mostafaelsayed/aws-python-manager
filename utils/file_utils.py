import json
import yaml
import os
import re

def write_json(response, file_name):
    with open(file_name, 'w') as file:
        file.write(json.dumps(response, indent=4, default=str))

def replace_values(obj, values):
    obj_str = json.dumps(obj)
    matches = re.findall(r"\<.*?\>", obj_str)
    for match in matches:
        match = match.replace('<', '')
        match = match.replace('>', '')
        obj_str = obj_str.replace('<' + match + '>', values[match])
    return json.loads(obj_str)


def parse(file_name):
    with open(file_name, 'r') as file:
        values = None
        try:
            dir_path = os.path.dirname(file_name)
            values_file_path = dir_path + '/values.yaml'
            try:
                with open(values_file_path, 'r') as values_file:
                    values = yaml.safe_load(values_file)
            except FileNotFoundError as e:
                print('no values found for ' + file_name)
            response = yaml.safe_load(file)
            if values != None:
                return replace_values(response, values)
            return response
        except FileNotFoundError as e:
            print('cannot parse file with name: ' + file_name + '. exception details: ', e)