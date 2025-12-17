from botocore.waiter import WaiterModel, create_waiter_with_client
import boto3
from clients.default_client import DefaultClient

def create_datasync_task_waiter(state):
    client = DefaultClient()
    instance = client.get_instance('datasync')
    waiter_name = "LifeCycleCompleted"
    waiter_config = {
        "version": 2,
        "waiters": {
            "LifeCycleCompleted": {
                "operation": "DescribeTask",
                "delay": 2, # Number of seconds to delay
                "maxAttempts": 5, # Max attempts before failure
                'acceptors': [
                    {
                        'matcher': 'path',
                        'argument': 'Status',
                        'expected': state,
                        'state': 'success'
                    }
                ]
            }
        }
    }
    waiter_model = WaiterModel(waiter_config)
    return create_waiter_with_client(waiter_name, waiter_model, instance)