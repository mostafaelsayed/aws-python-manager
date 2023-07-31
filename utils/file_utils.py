import json

def write_json(response, file_name):
    with open(file_name, 'w') as file:
        file.write(json.dumps(response, indent=4, default=str))