from botocore.waiter import WaiterModel, create_waiter_with_client

def create_mount_target_waiter(client, state):
    waiter_name = "LifeCycleCompleted"
    waiter_config = {
        "version": 2,
        "waiters": {
            "LifeCycleCompleted": {
                "operation": "DescribeMountTargets",
                "delay": 10, # Number of seconds to delay
                "maxAttempts": 10, # Max attempts before failure
                "acceptors": [
                    {
                        "matcher": "path",
                        "expected": state,
                        "argument": "MountTargets[0].LifeCycleState",
                        "state": "success"
                    }
                ]
            }
        }
    }
    waiter_model = WaiterModel(waiter_config)
    return create_waiter_with_client(waiter_name, waiter_model, client)