# Local Config Loader

A set of helper functions for loading local configuration files.

We build this library on [Hackt](https://hackt.app) to support local development of internal projects and [public apps in our catalog](https://hackt.app/catalog). Learn more about other open-source libraries on [lib.hackt.app](https://lib.hackt.app/).

Custom functions currently supported are related to Serverless projects on AWS, which is, at the moment, our primary cloud setup:

- [AWS SAM templates](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy.html)
- [AWS SAM local Lambda environment variables](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-invoke.html#serverless-sam-cli-using-invoke-environment-file)
- [DynamoDB local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html) (Docker) configuration templates.

---

## Runtime support

<img src="//logo.clearbit.com/python.org?size=120">

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

Documentation is available in the [repository wiki](https://github.com/hacktlib/py-local-config-loader/wiki).

---

## License

This library is licensed under [Apache 2.0](https://raw.githubusercontent.com/hacktlib/py-local-config-loader/main/LICENSE).

---

## Contributor guide

Please check out guidelines in the [repository wiki](https://github.com/hacktlib/py-local-config-loader/wiki).

---

## Acknowledgements

<a href="https://clearbit.com">Logos provided by Clearbit</a>
