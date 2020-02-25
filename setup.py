from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()
    
setup(
    name='CoordinateTransformations',
    version='0.8.8',
    packages=['CoordinateTransformations'],
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='',
    author='Parth Viradiya',
    author_email='parthviradiya08@gmail.com',
    license='MIT',
    classfiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: MIT License',        
    ],
    keywords=[
        'robotics', 'coordinate transformations', 'robot kinematics',
    ],
    install_requires = [
        "numpy > 1.5",
    ],    
    extras_require = {
        "dev": [
            "pytest >= 3.7",
        ],
    },
)
