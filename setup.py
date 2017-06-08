# -*- coding: utf-8 -*-
"""
Flask-RedLock
-------------------

Flask-RedLock
"""
import os
import re
from setuptools import setup


def find_version(fname):
    '''Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    '''
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version


__version__ = find_version(os.path.join("flask_redlock", "__init__.py"))

setup(
    name='Flask-Redlock',
    version=__version__,
    url='http://github.com/yoophi/flask-redlock/',
    license='MIT License',
    author='Pyunghyuk Yoo',
    author_email='yoophi@gmail.com',
    description='Redlock for Flask',
    long_description=__doc__,
    packages=['flask_redlock',
              ],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'redlock==1.2.0',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)