from clients.default_client import DefaultClient
client = DefaultClient()

def get_file_system_id_by_name(name):
    resource_group_tagging_instance = client.get_instance('resourcegroupstaggingapi')
    file_system = resource_group_tagging_instance.get_resources(
        TagFilters=[
            {'Key': 'file-system-name', 'Values': [name]}
        ]
    )
    print(file_system)
    file_system_id = file_system['ResourceTagMappingList'][0]['ResourceARN'].split('/')[-1]

    return file_system_id

def get_mount_target_id_by_file_system_name(name):
    instance = client.get_instance('efs')
    mount_targets = instance.describe_mount_targets(
        FileSystemId=get_file_system_id_by_name(name)
    )

    mount_targets = mount_targets['MountTargets']

    return mount_targets[0]['MountTargetId'] if mount_targets else None