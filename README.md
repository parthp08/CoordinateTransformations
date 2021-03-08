# CoordinateTransformations
Toolbox for Coordinate Transformations for Robotics Analysis.

Documentation: https://coordinatetransformations.readthedocs.io/en/latest/

## Installation

Run the following to install [older version, for latest changes please install directly from the repo]:

```python
pip install CoordinateTransformations
```

for installing directly from this repo
```python
pip install git+https://github.com/parthp08/CoordinateTransformations
```

## Usage

```python
from CoordinateTranformations import RotationMatrix, TrasformationMatrix

# Create Rotation Matrix object
R = RotationMatrix()

# Generate Rotation of 30 degree about X-axis
R.rotx(30, unit='deg')

# Convert Rotation Matrix to Euler Angles in degrees
alpha, beta, gamma = R.to_euler_angles(output_unit='deg')

# Get Rotation Matrix from Euler Angles
R2 = RotationMatrix()
R2.from_euler_rotation(alpha, beta, gamma, unit='deg', order='zyx')
```
for more example see tests files

# Developing CoordinateTransformations

To install CoordinateTransformations, along with tools you need to develop and run tests, run the following in your virtualenv:

```bash
pip install -e .[dev]
```
