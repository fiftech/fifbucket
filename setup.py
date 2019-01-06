import os
from setuptools import setup

VERSION_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'fifbucket', 'version.py')
VERSION = None
with open(VERSION_FILE, 'r') as f:
    VERSION = f.read().split()[2][1:-1]
with open('README.md') as f:
    long_description = f.read()

setup(
    name='fifbucket',
    packages=['fifbucket'],
    version=VERSION,
    description='Bitbucket Api Library',
    author='Mario Faundez',
    author_email='mariofaundez@hotmail.com',
    url='https://github.com/fiftech/fifbucket',
    download_url='https://github.com/fiftech/fifbucket/archive/{}.tar.gz'.format(VERSION),
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['bitbucket'],
    classifiers=[],
    install_requires=[
        'requests==2.21.0',
    ],
)
