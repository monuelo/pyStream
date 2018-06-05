#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Héricles Emanuel <hericles.me@gmail.com>

try:
    from setuptools import setup
except ImportError:
    from os import system
    system('pip install --user setuptools')
    from setuptools import setup

setup(
   name='pyStream',
   version='0.0.1',
   description='Python Streamer',
   license='MIT',
   classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
   url='https://github.com/hericlesme/pyStream',
   author='Héricles Emanuel',
   author_email='hericles.me@gmail.com',
   packages=['pyStream'],
   install_requires=['pillow', 'pyscreenshot', 'flask'],
)
