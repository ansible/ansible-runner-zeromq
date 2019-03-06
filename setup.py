#!/usr/bin/env python

# Copyright (c) 2018 Red Hat, Inc.
# All Rights Reserved.

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="ansible-runner-zeromq",
    version="1.0.0",
    author="Red Hat Ansible",
    url="https://github.com/ansible/ansible-runner-zeromq",
    license='Apache',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'pyzmq',
        'ansible-runner',
    ],
    entry_points={'ansible_runner.plugins': 'zeromq = ansible_runner_zeromq'},
    zip_safe=False,
)
