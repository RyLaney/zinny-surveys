"""setup.py for zinny-surveys package."""
from setuptools import setup, find_packages

setup(
    name='zinny-surveys',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    package_dir={"zinny_sruveys": "surveys"},
    package_data={
        '': ['surveys/**/*.json', 'weights/**/*.json']
    },
    description='Surveys and weights for Zinny.',
    url='https://github.com/RyLaney/zinny-surveys',
    author="Ryan Laney",
    license='BSD-3-Clause',
    python_requires=">=3",
)
