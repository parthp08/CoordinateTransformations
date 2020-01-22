from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='CoordinateTransformations',
    version='0.1',
    packages=['CoordinateTransformations'],
    long_description=readme(),
    long_description_content_type='md',
    url='',
    author='Parth Viradiya',
    author_email='parthviradiya08@gmail.com',
    license='MIT',
)
