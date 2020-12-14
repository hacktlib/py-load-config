from setuptools import setup
import pathlib


here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')


setup(
    name='config-loader',
    version='0.1.0b0',
    description='Helper functions for loading configuration files. Useful to test/debug using config parameters.',  # NOQA
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
    package_dir={'': 'config_loader'},
    python_requires='>=3.6, <4',
    install_requires=[
        'boto3>=1.16.30',
        'PyYAML>=5.3.1',
        'toml>=0.10.2',
    ],
    extras_require={
        'dev': [
            'pytest>=6.2.0',
            'coverage>=5.3',
            'coverage-badge>=1.0.1',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/hacktlib/py-config-loader/issues',  # NOQA
        'Say Thanks!': 'http://lib.hackt.app',
        'Source': 'https://github.com/hacktlib/py-config-loader/',
    },
)
