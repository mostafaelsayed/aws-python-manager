def attach_security_groups(config):
    if 'security_groups' in config:
        return config['security_groups']
    return []