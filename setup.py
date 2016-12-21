# coding=utf-8
import os
from distutils.spawn import find_executable
from setuptools import setup, find_packages
import sys

sys.path.append('./test')

from esfabric import __version__

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()


if os.path.exists(os.path.join(os.path.dirname(__file__), 'README.txt')):
    with open(os.path.join(os.path.dirname(__file__), 'README.txt')) as readme:
        README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as requirements:
    REQUIREMENTS = requirements.read().splitlines()

setup(
    name='elasticsearch-fabric',
    version=__version__,
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    license='MIT',
    author='Kunihiko Kido',
    author_email='kunihiko.kido@me.com',
    url='https://github.com/KunihikoKido/elasticsearch-fabric',
    description='This package provides a unified command line interface to Elasticsearch in Fabric.',
    long_description=README,
    platforms=['OS Independent'],
    keywords=['elasticsearch', 'fabric'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
    ],
    include_package_data=True,
    test_suite = "tasks_test.suite",
    scripts=['bin/es_bash_completion'],
)
