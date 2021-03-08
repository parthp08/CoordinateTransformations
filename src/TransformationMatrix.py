import numpy as np
from .RotationMatrix import RotationMatrix


class TransformationMatrix(RotationMatrix, object):

    def __init__(self):
        super().__init__
        self.set_rotation_matrix(np.eye(3))
        self._P = np.zeros((3,))
        self._T = np.eye(4)

    def __mul__(self, *transformations):
        for transformation in transformations:
            if self._is_transformation_matrix(transformation):
                self._add_transformation(transformation.get_transformation_matrix())
        return self

    def __repr__(self):
        return f"{self.get_transformation_matrix()}"

    def _add_translation(self, P):
        self.set_position(np.matmul(
            self.get_rotation_matrix(), P) + self.get_position())

    def _add_transformation(self, T):
        self._add_rotation(T[:3, :3])
        self._add_translation(T[:3, 3].reshape(3, 1))

    def get_transformation_matrix(self):
        self._T[:3,:3] = self.get_rotation_matrix()
        self._T[:3,3] = self.get_position().reshape(3,)
        return self._T

    def get_position(self):
        return self._P.reshape(3,1)

    def set_transformation_matrix(self, T):
        if T.shape == (4, 4):
            self.set_rotation_matrix(T[:3,:3])
            self.set_position(T[:3,3].reshape(3,1))
        else:
            raise "transformation matrix must be of size (4,4)"

    def set_position(self, P):
        if P.shape == (3, 1):
            self._P = P.reshape(3,)
        else:
            raise "position vector must be of size (3,1)"

    def inverse(self):
        self.inverse()
        self.set_position(-np.matmul(self.get_rotation_matrix(), self.get_position()))

    def translate(self, vector):
        self.set_position(self.get_position() + vector)

    def operate(self, vector):
        return np.matmul(self.get_rotation_matrix(), vector) + self.get_position()

    def screw_x(self, distance, angle, unit='rad'):
        self.rotx(angle, unit=unit)
        self.set_position(np.array([[distance], [0], [0]]))

    def screw_y(self, distance, angle, unit='rad'):
        self.roty(angle, unit=unit)
        self.set_position(np.array([[0], [distance], [0]]))

    def screw_z(self, distance, angle, unit='rad'):
        self.rotz(angle, unit=unit)
        self.set_position(np.array([[0], [0], [distance]]))

    @staticmethod
    def _is_transformation_matrix(T):
        return type(T) == TransformationMatrix
