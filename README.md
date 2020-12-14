# Load Config

![Test Coverage](https://raw.githubusercontent.com/hacktlib/py-load-config/main/coverage.svg)
![PyPI](https://img.shields.io/pypi/v/load-config)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Requirements Status](https://requires.io/github/hacktlib/py-load-config/requirements.svg?branch=main)](https://requires.io/github/hacktlib/py-load-config/requirements/?branch=main)
[![Code Style](https://img.shields.io/badge/code%20style-PEP8-lightgrey)](https://github.com/hhatto/autopep8/)
[![Code Formatter](https://img.shields.io/badge/formatter-autopep8-lightgrey)](https://github.com/hhatto/autopep8/)
[![Test Framework](https://img.shields.io/badge/testing-pytest-lightgrey)](https://github.com/pytest-dev/pytest/)

Helper functions for loading configuration files. Useful to test/debug using config parameters.

Custom functions currently supported:

- Load [AWS SAM template](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy.html)
- Load [AWS SAM configuration file](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-config.html)
- Load AWS SAM local Lambda [environment variables](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-invoke.html#serverless-sam-cli-using-invoke-environment-file)
- Load [DynamoDB local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html) (Docker) configuration templates

> We built this library in [Hackt](https://hackt.app) to support local development of internal projects and [public apps in our catalog](https://hackt.app/catalog). Learn more about other open-source libraries on [lib.hackt.app](https://lib.hackt.app/).

---

# Runtime support

![Python Logo](https://logo.clearbit.com/python.org?size=120)

> This is the Python runtime library, compatible with Python3.6+. Currently there isn't support for other runtimes. A Javascript/nodejs version is planned, but unscheduled.

---

# Installation and Usage

Install with pip: `pip install load-config`

Load [AWS SAM template](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy.html) file:

```python
import load_config

template = load_config.sam_template()

env_vars = template['Resources']['MyFunction']['Environment']['Variables']
```

By default, `load_config` will look for SAM templates in `./template.yaml`. Optionally, specify a different path:

```python
template = load_config.sam_template(filepath='my-project/template.yml')
```

---

## Documentation

Documentation is available in the [repository wiki](https://github.com/hacktlib/py-load-config/wiki).

---

## License

This library is licensed under [Apache 2.0](https://raw.githubusercontent.com/hacktlib/py-load-config/main/LICENSE).

---

## Contributor guide

Please check out guidelines in the [repository wiki](https://github.com/hacktlib/py-load-config/wiki).

---

## Acknowledgements

[Published & supported by **Hackt App**](https://hackt.app)

[Logos provided by **Clearbit**](https://clearbit.com)
