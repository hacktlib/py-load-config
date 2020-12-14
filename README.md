# About Config Loader

![Test Coverage](https://raw.githubusercontent.com/hacktlib/py-config-loader/main/coverage.svg)

Helper functions for loading configuration files. Useful to test/debug using config parameters.

Custom functions currently supported:

- Load [AWS SAM template](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy.html)
- Load AWS SAM local Lambda [environment variables](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-invoke.html#serverless-sam-cli-using-invoke-environment-file)
- Load [DynamoDB local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html) (Docker) configuration templates

> We build this library on [Hackt](https://hackt.app) to support local development of internal projects and [public apps in our catalog](https://hackt.app/catalog). Learn more about other open-source libraries on [lib.hackt.app](https://lib.hackt.app/).

---

# Runtime support

![Python Logo](https://logo.clearbit.com/python.org?size=120)

> This is the Python runtime library, compatible with Python3.6+. Currently there isn't support for other runtimes. A Javascript/nodejs version is planned, but unscheduled.

---

# Installation and Usage

Install with pip: `pip install local-config-loader`

Load [AWS SAM template](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy.html) file:

```python
from local_config_loader import load_sam_template

template = load_sam_template('template.yaml')

env_vars = template['Resources']['MyFunction']['Environment']['Variables']
```

---

## Documentation

Documentation is available in the [repository wiki](https://github.com/hacktlib/py-config-loader/wiki).

---

## License

This library is licensed under [Apache 2.0](https://raw.githubusercontent.com/hacktlib/py-config-loader/main/LICENSE).

---

## Contributor guide

Please check out guidelines in the [repository wiki](https://github.com/hacktlib/py-config-loader/wiki).

---

## Acknowledgements

<a href="https://clearbit.com">Logos provided by Clearbit</a>
