from setuptools import setup, find_packages

setup(
    name='zinny-surveys',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'zinny_surveys': ['surveys/**/*.json', 'weights/**/*.json']
    },
    description='Surveys and weights for the-zinny',
    url='https://github.com/RyLaney/zinny-surveys',
    author='the-zinny Team',
    license='BSD-3-Clause',
)
