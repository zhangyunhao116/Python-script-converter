#!/usr/bin/env python
from setuptools import setup, find_packages

PROJECT_NAME = 'python-script-converter'
MODULE_NAME = 'psc'

setup(
    name='python-script-converter',
    version='1.1',

    author='ZhangYunHao',
    author_email='workvl@163.com',

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
