import json

import pytest

from load_config import (
    dynamodb_local,
    general_loader,
    lambda_environ,
    sam_all,
    sam_config,
    sam_template,
)


def test_general_loader():
    content = general_loader(
        filepath='tests/dummy_files/sample.json',
        loader=json.loads,
    )

    assert type(content) is dict
    assert 'hello' in content.keys()
    assert content['hello'] == 'world'


def test_general_loader_raises_filenotfound():
    with pytest.raises(FileNotFoundError):
        general_loader(filepath='xyz', loader=json.loads)


def test_sam_template():
    template = sam_template(
        filepath='tests/dummy_files/aws-sam-template.yaml',
    )

    assert type(template) is dict

    assert template.get('AWSTemplateFormatVersion') == '2010-09-09'
    assert template.get('Transform') == 'AWS::Serverless-2016-10-31'
    assert template \
        .get('Resources', {}) \
        .get('DummyFunction', {}) \
        .get('Type') == 'AWS::Serverless::Function'


def test_sam_config():
    config = sam_config(
        filepath='tests/dummy_files/aws-sam-config.toml',
    )

    assert type(config) is dict

    assert config.get('version') == 0.1
    assert config \
        .get('default', {}) \
        .get('deploy', {}) \
        .get('parameters', {}) \
        .get('stack_name') == 'dummy-function'


def test_sam_config_parameters():
    config = sam_config(
        filepath='tests/dummy_files/aws-sam-config-parameters.toml',
    )

    params = config['default']['deploy']['parameters'] \
        .get('parameter_overrides')

    assert type(params) is dict
    assert len(params.keys()) == 2
    assert params.get('DummyParameter') == 'abc-123'
    assert params.get('AnotherParameter') == 'Hello=World!'


def test_load_sam():
    sam_template_path = 'tests/dummy_files/aws-sam-template.yaml'
    sam_config_path = 'tests/dummy_files/aws-sam-config.toml'

    sam = sam_all(
        template_filepath=sam_template_path,
        config_filepath=sam_config_path,
    )

    expected_template = sam_template(filepath=sam_template_path)
    expected_config = sam_config(filepath=sam_config_path)

    assert hasattr(sam, 'template')
    assert hasattr(sam, 'config')
    assert sam.template == expected_template
    assert sam.config == expected_config


def test_dynamodb():
    ddb = dynamodb_local(
        filepath='tests/dummy_files/aws-dynamodb-local.yaml',
    )

    assert type(ddb) is dict
    assert ddb.get('port') == '8000'
    assert ddb \
        .get('config', {}) \
        .get('container_name') == 'dummy-dynamodb-container'
    assert ddb \
        .get('config', {}) \
        .get('ports') == ['8000:8000']


def test_lambda_env():
    try:
        env = lambda_environ(
            function_name='DummyFunction',
            filepath='tests/dummy_files/aws-sam-lambda-local-env-vars.json',
        )
    except KeyError:
        pytest.fail('Unexpected KeyError')

    assert type(env) is dict
    assert env.get('HELLO') == 'World!'


def test_lambda_env_keyerror_raised():
    with pytest.raises(KeyError):
        lambda_environ(
            function_name='InexistentFunction',
            filepath='tests/dummy_files/aws-sam-lambda-local-env-vars.json',
            fail_on_keyerror=True,
        )


def test_lambda_env_keyerror_not_raised():
    try:
        lambda_environ(
            function_name='InexistentFunction',
            filepath='tests/dummy_files/aws-sam-lambda-local-env-vars.json',
            fail_on_keyerror=False,
        )
    except KeyError:
        pytest.fail('Unexpected KeyError')
