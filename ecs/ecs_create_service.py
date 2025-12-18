from clients.default_client import DefaultClient
from utils.file_utils import parse
from utils.common_utils import attach_ecs_service_connect_services
client = DefaultClient()
instance = client.get_instance('ecs')
reference = parse('ecs/task-configuration/current.yaml')['task_reference']
service_config = parse('ecs/service-configuration/{0}/service_config.yaml'.format(reference))
response = instance.create_service(
    cluster=service_config['cluster'],
    serviceName=service_config['service_name'],
    taskDefinition=service_config['task_definition'],
    # availabilityZoneRebalancing=service_config['availability_zone_rebalancing'],
    # loadBalancers=[
    #     {
    #         'targetGroupArn': 'string',
    #         'loadBalancerName': 'string',
    #         'containerName': 'string',
    #         'containerPort': 123,
    #         'advancedConfiguration': {
    #             'alternateTargetGroupArn': 'string',
    #             'productionListenerRule': 'string',
    #             'testListenerRule': 'string',
    #             'roleArn': 'string'
    #         }
    #     },
    # ],
    # serviceRegistries=[
    #     {
    #         'registryArn': 'string',
    #         'port': 123,
    #         'containerName': 'string',
    #         'containerPort': 123
    #     },
    # ],
    desiredCount=service_config['desired_count'],
    # clientToken='string',
    launchType=service_config['launch_type'],
    # capacityProviderStrategy=[
    #     {
    #         'capacityProvider': 'string',
    #         'weight': 123,
    #         'base': 123
    #     },
    # ],
    # platformVersion='string',
    # role='string',
    # deploymentConfiguration={
    #     'deploymentCircuitBreaker': {
    #         'enable': True|False,
    #         'rollback': True|False
    #     },
    #     'maximumPercent': 123,
    #     'minimumHealthyPercent': 123,
    #     'alarms': {
    #         'alarmNames': [
    #             'string',
    #         ],
    #         'rollback': True|False,
    #         'enable': True|False
    #     },
    #     'strategy': 'ROLLING'|'BLUE_GREEN'|'LINEAR'|'CANARY',
    #     'bakeTimeInMinutes': 123,
    #     'lifecycleHooks': [
    #         {
    #             'hookTargetArn': 'string',
    #             'roleArn': 'string',
    #             'lifecycleStages': [
    #                 'RECONCILE_SERVICE'|'PRE_SCALE_UP'|'POST_SCALE_UP'|'TEST_TRAFFIC_SHIFT'|'POST_TEST_TRAFFIC_SHIFT'|'PRODUCTION_TRAFFIC_SHIFT'|'POST_PRODUCTION_TRAFFIC_SHIFT',
    #             ],
    #             'hookDetails': {...}|[...]|123|123.4|'string'|True|None
    #         },
    #     ],
    #     'linearConfiguration': {
    #         'stepPercent': 123.0,
    #         'stepBakeTimeInMinutes': 123
    #     },
    #     'canaryConfiguration': {
    #         'canaryPercent': 123.0,
    #         'canaryBakeTimeInMinutes': 123
    #     }
    # },
    # placementConstraints=[
    #     {
    #         'type': 'distinctInstance'|'memberOf',
    #         'expression': 'string'
    #     },
    # ],
    # placementStrategy=[
    #     {
    #         'type': 'random'|'spread'|'binpack',
    #         'field': 'string'
    #     },
    # ],
    networkConfiguration={
        'awsvpcConfiguration': {
            'subnets': service_config['subnet_ids'],
            'securityGroups': service_config['security_groups'],
            'assignPublicIp': service_config['assign_public_ip']
        }
    },
    # healthCheckGracePeriodSeconds=123,
    schedulingStrategy=service_config['scheduling_strategy'],
    deploymentController={
        'type': service_config['deployment_controller_type']
    },
    tags=service_config['tags'],
    # enableECSManagedTags=True|False,
    # propagateTags='TASK_DEFINITION'|'SERVICE'|'NONE',
    # enableExecuteCommand=True|False,
    serviceConnectConfiguration={
        'enabled': service_config['service_connect_configuration']['enabled'],
        'namespace': service_config['service_connect_configuration']['namespace'],
        'services': attach_ecs_service_connect_services(service_config['service_connect_configuration']),
        # 'logConfiguration': {
        #     'logDriver': 'json-file'|'syslog'|'journald'|'gelf'|'fluentd'|'awslogs'|'splunk'|'awsfirelens',
        #     'options': {
        #         'string': 'string'
        #     },
        #     'secretOptions': [
        #         {
        #             'name': 'string',
        #             'valueFrom': 'string'
        #         },
        #     ]
        # },
        # 'accessLogConfiguration': {
        #     'format': 'TEXT'|'JSON',
        #     'includeQueryParameters': 'DISABLED'|'ENABLED'
        # }
    },
    # volumeConfigurations=[
    #     {
    #         'name': 'string',
    #         'managedEBSVolume': {
    #             'encrypted': True|False,
    #             'kmsKeyId': 'string',
    #             'volumeType': 'string',
    #             'sizeInGiB': 123,
    #             'snapshotId': 'string',
    #             'volumeInitializationRate': 123,
    #             'iops': 123,
    #             'throughput': 123,
    #             'tagSpecifications': [
    #                 {
    #                     'resourceType': 'volume',
    #                     'tags': [
    #                         {
    #                             'key': 'string',
    #                             'value': 'string'
    #                         },
    #                     ],
    #                     'propagateTags': 'TASK_DEFINITION'|'SERVICE'|'NONE'
    #                 },
    #             ],
    #             'roleArn': 'string',
    #             'filesystemType': 'ext3'|'ext4'|'xfs'|'ntfs'
    #         }
    #     },
    # ],
    # vpcLatticeConfigurations=[
    #     {
    #         'roleArn': 'string',
    #         'targetGroupArn': 'string',
    #         'portName': 'string'
    #     },
    # ]
)

print(response)