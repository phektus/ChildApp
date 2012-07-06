#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='childapp',
      version='0.1',
      packages=find_packages(),
      package_data={'childapp': ['bin/*.*', 'static/*.*', 'templates/*.*']},
      exclude_package_data={'childapp': ['bin/*.pyc']},
      scripts=['childapp/bin/manage.py'])
