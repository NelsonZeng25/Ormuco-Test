from setuptools import setup, find_packages

setup(
    name='version_compare',
    version='0.0.1',
    description='A simply library with the function compare() that can compare two valid version string',
    license='MIT',
    packages=find_packages(exclude=['test_compare']),
    author='Nelson Zeng',
    author_email= 'nelson.zeng25@gmail.com',
    keywords=['compare'],
    url='https://github.com/NelsonZeng25/Ormuco-Test/tree/master/Q2-VersionString'
)