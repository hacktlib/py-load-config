from functools import partial

import yaml

from load_config.constants import AWS_CUSTOM_YAML_CONSTRUCTOR_NAMES


def aws_yaml_constructor(loader, node):
    return loader.construct_scalar(node)


for aws_constructor_name in AWS_CUSTOM_YAML_CONSTRUCTOR_NAMES:
    yaml.SafeLoader.add_constructor(aws_constructor_name, aws_yaml_constructor)

yaml_safe_load = partial(yaml.load, Loader=yaml.SafeLoader)
