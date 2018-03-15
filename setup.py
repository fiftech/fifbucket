from setuptools import setup, find_packages

setup(
    name='fifbucket',
    packages=find_packages(exclude=['venv*']),
    version='0.7',
    description='Bitbucket Api Library',
    author='Mario Faundez',
    author_email='mariofaundez@hotmail.com',
    url='https://github.com/ordenador/fifbucket',
    download_url='https://github.com/ordenador/fifbucket/archive/0.7.tar.gz',
    license='MIT',
    keywords=['bitbucket'],
    classifiers=[],
    install_requires=[
        'requests==2.18.4',
    ],
)
