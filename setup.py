from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='fifbucket',
    packages=['fifbucket'],
    version='0.9',
    description='Bitbucket Api Library',
    author='Mario Faundez',
    author_email='mariofaundez@hotmail.com',
    url='https://github.com/fiftech/fifbucket',
    download_url='https://github.com/fiftech/fifbucket/archive/0.9.tar.gz',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['bitbucket'],
    classifiers=[],
    install_requires=[
        'requests==2.21.0',
    ],
)
