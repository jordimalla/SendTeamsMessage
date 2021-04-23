import os
from setuptools import setup
from SendTeamsMessage import __version__

setup(
    name='SendTeamsMessage',
    version=__version__,
    description='A package to send a little message to your Teams channel',
    url='git@github.com:jordimalla/SendTeamsMessage.git',
    author='Jordi Malla',
    license='MIT',
    packages=['SendTeamsMessage'],
    scripts=['bin/SendTeamsMessage'],
    long_description=open_file('README.rst').read(),
    install_requires=open_file('requirements.txt').readlines(),
    zip_safe=True
)
