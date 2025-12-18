def attach_security_groups(config):
    if 'security_groups' in config:
        return config['security_groups']
    return []

def attach_ecs_service_connect_services(config):
    if 'services' in config:
        return config['services']
    return []