import numpy as np
from .transformation_matrix import TransformationMatrix


class RotationMatrix(TransformationMatrix, object):

    def __init__(self):
        super().__init__
        self._R = np.eye(3)

    @staticmethod
    def _is_rotation_matrix(R):
        return type(R) == RotationMatrix

    def _add_rotation(self, R):
        # update self.R
        self._R = np.matmul(self._R, R)

    def set_R(self, R):
        if self._is_rotation_matrix(R) or R.shape == (3, 3):
            self._R = R
        else:
            raise "rotation matrix must be of shape (3,3) or RotationMatrix type"

    def __mul__(self, *rotations):
        for rotation in rotations:
            if self._is_rotation_matrix(rotation):
                self._add_rotation(rotation.get_R())
        return self

    def inverse(self):
        self._R = self._R.T

    def operate_on_point(self, point):
        return np.matmul(self._R, point)

    def to_transformation_matrix(self):
        T = np.eye(4)
        T[:3, :3] = self._R
        return T
