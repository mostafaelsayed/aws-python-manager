from clients.default_client import DefaultClient
from utils.file_utils import parse

def create_code_pipeline():
    client = DefaultClient()
    instance = client.get_instance('codepipeline')
    env = client.get_env()
    role_name = 'codepipeline'
    response = instance.create_pipeline(
        pipeline={
            'artifactStore': {
                'type': 'S3',
                'location': 'organizer-pipeline-artifacts'
            },
            'name': 'organizer-pipeline',
            'roleArn': 'arn:aws:iam::{0}:role/{1}'.format(env['aws_account_id'], role_name),
            'stages': [
                {
                    'name': 'Source',
                    'actions': [
                        {
                            'name': 'input',
                            'actionTypeId': {
                                'category': 'Source',
                                'owner': 'ThirdParty',
                                'provider': 'Github',
                                'version': '1'
                            }
                        },
                    ]
                },
                {
                    'name': 'Build',
                    'actions': [
                        {
                            'name': 'input',
                            'actionTypeId': {
                                'category': 'Build',
                                'owner': 'ThirdParty',
                                'provider': 'Github',
                                'version': '1'
                            }
                        },
                    ]
                }
            ],
            'version': 1,
            'pipelineType': 'V1',
            'triggers': [
                {
                    'providerType': 'CodeStarSourceConnection',
                    'gitConfiguration': {
                        'sourceActionName': 'input'
                    }
                },
            ]
        },
        tags=[
            {
                'key': 'app',
                'value': 'organizer'
            },
        ]
    )

    print(response)

create_code_pipeline()