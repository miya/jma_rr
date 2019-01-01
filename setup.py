import os
from setuptools import setup, find_packages

install_reqs = [line.strip() for line in open('requirements.txt').readlines()]

setup(
    name='rainfall',
    version='0.1',
    description='Create precipitation information gif of JAM',
    url='https://github.com/0x0u/rainfall',
    author='m0zu',
    author_email='m0zurillex@gmail.com',
    install_requires=install_reqs,
    classifiers=['Programming Language :: Python :: 3.6']
)
