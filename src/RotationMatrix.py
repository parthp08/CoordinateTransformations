import numpy as np


class RotationMatrix(object):

    def __init__(self):
        self._R = np.eye(3)

    def __mul__(self, *rotations):
        for rotation in rotations:
            if self._is_rotation_matrix(rotation):
                self._add_rotation(rotation.get_rotation_matrix())
        return self
    
    def __repr__(self):
        return f"{self.get_rotation_matrix()}"

    def _add_rotation(self, R):
        self.set_rotation_matrix(np.matmul(self.get_rotation_matrix(), R))

    def get_rotation_matrix(self):
        return self._R

    def set_rotation_matrix(self, R):
        if self._is_rotation_matrix(R) or R.shape == (3, 3):
            self._R = R
        else:
            raise "rotation matrix must be of shape (3,3) or RotationMatrix type"

    def to_transformation_matrix(self):
        T = np.eye(4)
        T[:3, :3] = self.get_rotation_matrix()
        return T

    def inverse(self):
        self.set_rotation_matrix(self.get_rotation_matrix().T)

    def rotx(self, angle, unit='rad'):
        if unit.lower() == 'deg':
            angle = np.deg2rad(angle)

        s_angle, c_angle = np.sin(angle), np.cos(angle)

        self._add_rotation(np.array([
            [1, 0, 0],
            [0, c_angle, -s_angle],
            [0, s_angle, c_angle]
        ]))

    def roty(self, angle, unit='rad'):
        if unit.lower() == 'deg':
            angle = np.deg2rad(angle)

        s_angle, c_angle = np.sin(angle), np.cos(angle)

        self._add_rotation(np.array([
            [c_angle, 0, s_angle],
            [0, 1, 0],
            [-s_angle, 0, c_angle]
        ]))

    def rotz(self, angle, unit='rad'):
        if unit.lower() == 'deg':
            angle = np.deg2rad(angle)

        s_angle, c_angle = np.sin(angle), np.cos(angle)

        self._add_rotation(np.array([
            [c_angle, -s_angle, 0],
            [s_angle, c_angle, 0],
            [0, 0, 1]
        ]))

    def operate(self, vector):
        return np.matmul(self.get_rotation_matrix(), vector)

    def from_fixed_rotation(self, angle_x, angle_y, angle_z, unit='rad'):
        self.rotz(angle_z, unit=unit)
        self.roty(angle_y, unit=unit)
        self.rotx(angle_x, unit=unit)

    def from_euler_rotation(self, alpha, beta, gamma, unit='rad', order='zyx'):
        assert order[0] != order[1] and order[1] != order[2], \
            "order choice is constrained to not have two succesive rotation\
                 with same axis such as xxy or xzz"

        angle_list = [alpha, beta, gamma]
        i = 0
        for axis in order:
            if axis == 'x':
                self.rotx(angle_list[i], unit=unit)
            elif axis == 'y':
                self.roty(angle_list[i], unit=unit)
            elif axis == 'z':
                self.rotz(angle_list[i], unit=unit)
            i += 1

    def from_axis_angle_rotation(self, vector, theta, unit='rad'):
        if unit.lower() == "deg":
            theta = np.deg2rad(theta)

        K = vector / np.linalg.norm(vector)
        kx, ky, kz = K[0, 0], K[1, 0], K[2, 0]
        s_theta, c_theta = np.sin(theta), np.cos(theta)
        v_theta = 1 - c_theta

        self._add_rotation(np.array([
            [(kx**2)*v_theta + c_theta, kx*ky*v_theta -
             kz*s_theta, kx*kz*v_theta + ky*s_theta],
            [kx*ky*v_theta + kz*s_theta,
             (ky**2)*v_theta + c_theta, ky*kz*v_theta - kx*s_theta],
            [kx*kz*v_theta - ky*s_theta, ky*kz*v_theta +
             kx*s_theta, (kz**2)*v_theta + c_theta]
        ]))

    def to_euler_angles(self, output_unit='rad'):
        """
        euler angle order : Z-Y-X
        """
        R = self.get_rotation_matrix()
        beta = np.arctan2(-R[2, 0],
                          np.sqrt(R[0, 0]**2 + R[1, 0]**2))
        if beta == np.deg2rad(90):
            alpha = 0
            gamma = np.arctan2(R[0, 1], R[1, 1])

            if output_unit == 'deg':
                return self._output_deg(alpha, beta, gamma)
            return (alpha, beta, gamma)

        elif beta == np.deg2rad(-90):
            alpha = 0
            gamma = -np.arctan2(R[0, 1], R[1, 1])

            if output_unit == 'deg':
                return self._output_deg(alpha, beta, gamma)
            return (alpha, beta, gamma)

        c_beta = np.cos(beta)
        alpha = np.arctan2(R[1, 0]/c_beta, R[0, 0]/c_beta)
        gamma = np.arctan2(R[2, 1]/c_beta, R[2, 2]/c_beta)

        if output_unit == 'deg':
            return self._output_deg(alpha, beta, gamma)
        return alpha, beta, gamma

    def to_axis_angle(self, output_unit='rad'):
        R = self.get_rotation_matrix()
        # always calculate the angle between 0 to 180
        theta = np.arccos((R[0, 0]+R[1, 1]+R[2, 2]-1)/2)

        # doesnt work for theta = 0 or 180 degrees
        K_hat = (1/(2*np.sin(theta))) * np.array([
            [R[2, 1] - R[1, 2]],
            [R[0, 2] - R[2, 0]],
            [R[1, 0] - R[0, 1]]
        ])

        if output_unit.lower() == "deg":
            return K_hat, np.rad2deg(theta)
        return K_hat, theta

    @staticmethod
    def _output_deg(alpha, beta, gamma):
        """ convert rad to deg """
        return (np.rad2deg(alpha), np.rad2deg(beta), np.rad2deg(gamma))

    @staticmethod
    def _is_rotation_matrix(R):
        return type(R) == RotationMatrix
