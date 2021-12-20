#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read().replace('\r\n', '\n')


setup(
    name='WestJR',
    version='0.3',
    license='Unlicense',
    description='Handling of train operation information of JR West, a railroad company in Japan',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='unyacat',
    author_email='admin@unyacat.net',
    url='https://github.com/unyacat/westjr',
    install_requires=['requests'],
    packages=find_packages(),
    keywords='westjr'
)