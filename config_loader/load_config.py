from collections import namedtuple
import json
import pathlib
from typing import NamedTuple, Union

import toml
import yaml

from custom_yaml import yaml_safe_load
import default_filepath as fp


def sam_all(
        template_filepath: Union[str, pathlib.Path] = fp.AWS_SAM_TEMPLATE,
        config_filepath: Union[str, pathlib.Path] = fp.AWS_SAM_CONFIG,
        loader: Union[json.loads, yaml.load] = yaml_safe_load,
        ) -> NamedTuple:
    '''Provide contents from both AWS SAM local Template and Config files

    Returns a nametuple with two attributes:
        - `template` (equivalent to `sam_template` function)
        - `config` (equivalent to `sam_config` function)
    '''
    sam = namedtuple('sam', 'template config')
    return sam(
        template=sam_template(filepath=template_filepath),
        config=sam_config(filepath=config_filepath),
    )


def sam_template(
        filepath: Union[str, pathlib.Path] = fp.AWS_SAM_TEMPLATE,
        loader: Union[json.loads, yaml.load] = yaml_safe_load,
        ) -> dict:
    '''Provide local SAM Template file contents'''
    return general_loader(filepath=filepath, loader=loader)


def sam_config(
        filepath: Union[str, pathlib.Path] = fp.AWS_SAM_CONFIG,
        loader: toml.loads = toml.loads,
        ) -> dict:
    '''Provide local SAM deployment Configuration file contents'''
    return general_loader(filepath=filepath, loader=loader)


def dynamodb_local(
        filepath: Union[str, pathlib.Path] = fp.AWS_DYNAMODB_LOCAL_TEMPLATE,
        loader: yaml.load = yaml_safe_load,
        ) -> dict:
    '''Provides DynamoDB local port number and other Docker config params'''
    ddb = general_loader(filepath=filepath, loader=loader)
    ddb_config = ddb['services']['dynamodb-local']
    ddb_port = ddb_config['ports'][0].split(':')[0]

    return {
        'port': ddb_port,
        'config': ddb_config,
    }


def lambda_environ(
        function_name: str,
        filepath: Union[str, pathlib.Path] = fp.AWS_SAM_LAMBDA_ENV_VARS,
        loader: json.loads = json.loads,
        fail_on_keyerror: bool = False,
        ) -> dict:
    '''Load local environment variables for a given Lambda function

    By default, will look for local-env-vars.json file. Optionally customize
    with the `filepath` argument.

    If the function name is not found in the json file, returna an empty dict.
    Pass `fail_on_keyerror=True` argument to raise an exception, instead.
    '''
    content = general_loader(filepath=filepath, loader=loader)

    try:
        return content[function_name]
    except KeyError as exc:
        if fail_on_keyerror:
            raise exc
        else:
            return {}


def general_loader(
        filepath: Union[str, pathlib.Path],
        loader: Union[json.loads, toml.loads, yaml.load],
        ) -> Union[dict, NamedTuple]:
    '''Thin wrapper for open python function embedded with a data pre-loader'''
    with open(filepath, 'r') as file:
        return loader(file.read())
