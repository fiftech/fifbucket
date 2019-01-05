from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='fifbucket',
    packages=find_packages(exclude=['venv*']),
    version='0.8',
    description='Bitbucket Api Library',
    author='Mario Faundez',
    author_email='mariofaundez@hotmail.com',
    url='https://github.com/fiftech/fifbucket',
    download_url='https://github.com/fiftech/fifbucket/archive/0.8.tar.gz',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['bitbucket'],
    classifiers=[],
    install_requires=[
        'requests==2.21.0',
    ],
)
