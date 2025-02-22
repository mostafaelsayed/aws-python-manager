from botocore.waiter import WaiterModel, create_waiter_with_client

def create_efs_waiter(client, state):
    waiter_name = "LifeCycleCompleted"
    waiter_config = {
        "version": 2,
        "waiters": {
            "LifeCycleCompleted": {
                "operation": "DescribeFileSystems",
                "delay": 2, # Number of seconds to delay
                "maxAttempts": 5, # Max attempts before failure
                'acceptors': [
                    {
                        'matcher': 'path',
                        'argument': 'FileSystems[0].LifeCycleState',
                        'expected': state,
                        'state': 'success'
                    }
                ]
            }
        }
    }
    waiter_model = WaiterModel(waiter_config)
    return create_waiter_with_client(waiter_name, waiter_model, client)