from setuptools import setup
import pathlib


here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')


setup(
    name='local-config-loader',
    version='0.1.0b0',
    description='A set of helper functions for loading local configuration files.',  # NOQA
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hacktlib/py-local-config-loader/wiki',
    author='Hackt.app',
    author_email='opensource@hackt.app',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
    py_modules=['config_loader'],
    python_requires='>=3.6, <4',
    install_requires=[
        'boto3>=1.16.30',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/hacktlib/py-local-config-loader/issues',  # NOQA
        'Say Thanks!': 'http://lib.hackt.app',
        'Source': 'https://github.com/hacktlib/py-local-config-loader/',
    },
)
