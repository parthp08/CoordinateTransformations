# CoordinateTransformations
Toolbox for Coordinate Transformations for Robotics Analysis.

## Installation

Run the following to install:

```python
pip install git+https://github.com/parthp08/CoordinateTransformations
```

## Usage

```python
from CoordinateTranformations import R_x, R2T

# Generate Rotation of 30 degree about X-axis
R_x(30, unit='deg')

# Generate Homogeneous Transformation matrix from rotation matrix"
R2T(R_x(30, unit='deg'))
```

# Developing CoordinateTransformations

To install CoordinateTransformations, along with tools you need to develop and run tests, run the following in your virtualenv:

```bash
pip install -e .[dev]
```
