from functools import partial
from unittest.mock import Mock

from load_config.constants import AWS_CUSTOM_YAML_CONSTRUCTOR_NAMES
from load_config.custom_yaml import aws_yaml_constructor, yaml


def test_yaml_dummy_aws_constructor_function():
    loader = Mock()
    loader.construct_scalar = Mock(return_value='construct_scalar')

    node = Mock()

    response = aws_yaml_constructor(loader, node)

    assert response == 'construct_scalar'
    loader.construct_scalar.assert_called_once_with(node)


def test_yaml_add_constructors():
    for name in AWS_CUSTOM_YAML_CONSTRUCTOR_NAMES:
        assert name in yaml.SafeLoader.yaml_constructors.keys()


def test_yaml_safe_loader():
    import yaml
    from load_config.custom_yaml import yaml_safe_load

    assert isinstance(yaml_safe_load, partial)
    assert yaml_safe_load.func == yaml.load
    assert 'Loader' in yaml_safe_load.keywords.keys()
    assert yaml_safe_load.keywords['Loader'] == yaml.SafeLoader
