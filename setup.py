from setuptools import setup, find_packages

setup(
    name='fipl_config',
    version='0.1',
    packages=find_packages(),
    install_requires=[
    'pydantic==2.5.3'
    ],
)