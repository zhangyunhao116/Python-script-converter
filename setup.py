#!/usr/bin/env python
import os
import sys
from setuptools import setup, find_packages

# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('pip3 install twine')
    os.system('pip3 install wheel')
    os.system('python3 setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    os.system('rm -rf build dist .egg zmail.egg-info')
    sys.exit()

PROJECT_NAME = 'python-script-converter'
MODULE_NAME = 'psc'

setup(
    name='python-script-converter',
    version='1.2',

    author='ZhangYunHao',
    author_email='zyunhjob@163.com',

    description='This is a tiny tool used to convert a python script to a executable file(only for Mac and Linux).',
    long_description='This is a tiny tool used to convert a python script to a executable file(only for Mac and Linux)',
    keywords='python tool converter',

    url='https://github.com/ZYunH/Python-script-converter',
    license="MIT Licence",

    platforms='Mac Linux',

    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'psc = psc.__main__:main'
        ]
    }

)
