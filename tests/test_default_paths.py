from importlib import reload
import os
from unittest import mock

import default_filepath as fp


def test_default_paths():
    assert fp.AWS_SAM_TEMPLATE == fp.DEFAULT['AWS_SAM_TEMPLATE']
    assert fp.AWS_SAM_CONFIG == fp.DEFAULT['AWS_SAM_CONFIG']
    assert fp.AWS_SAM_LAMBDA_ENV_VARS == fp.DEFAULT['AWS_SAM_LAMBDA_ENV_VARS']
    assert fp.AWS_DYNAMODB_LOCAL_TEMPLATE == fp.DEFAULT['AWS_DYNAMODB_LOCAL_TEMPLATE']  # NOQA


def test_custom_path_from_environ():
    DUMMY_SAM_TEMPLATE_PATH = 'DUMMY_SAM_TEMPLATE_PATH.yaml'
    DUMMY_SAM_CONFIG_PATH = 'DUMMY_SAM_CONFIG_PATH.toml'
    DUMMY_LAMBDA_ENV_VARS_PATH = 'DUMMY_LAMBDA_ENV_VARS_PATH.json'
    DUMMY_DYNAMODB_LOCAL_PATH = 'DUMMY_DYNAMODB_LOCAL_PATH.yaml'

    new_environ = {
        'AWS_SAM_TEMPLATE_PATH': DUMMY_SAM_TEMPLATE_PATH,
        'AWS_SAM_CONFIG_PATH': DUMMY_SAM_CONFIG_PATH,
        'AWS_SAM_LAMBDA_ENV_VARS_PATH': DUMMY_LAMBDA_ENV_VARS_PATH,
        'AWS_DYNAMODB_LOCAL_TEMPLATE_PATH': DUMMY_DYNAMODB_LOCAL_PATH,
    }

    with mock.patch.dict(os.environ, new_environ):
        reload(fp)

        assert fp.AWS_SAM_TEMPLATE == DUMMY_SAM_TEMPLATE_PATH
        assert fp.AWS_SAM_CONFIG == DUMMY_SAM_CONFIG_PATH
        assert fp.AWS_SAM_LAMBDA_ENV_VARS == DUMMY_LAMBDA_ENV_VARS_PATH
        assert fp.AWS_DYNAMODB_LOCAL_TEMPLATE == DUMMY_DYNAMODB_LOCAL_PATH
