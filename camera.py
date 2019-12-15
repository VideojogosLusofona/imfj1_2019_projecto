import numpy as np
from object3d import *

class Camera(Object3d):
    def __init__(self, ortho, res_x, res_y):
        super().__init__(self)

        self.ortho = ortho
        self.res_x = res_x
        self.res_y = res_y
        self.fov = math.radians(60)

    def get_projection_matrix(self):
        self.proj_matrix = np.zeros((4, 4))
        if (self.ortho):
            self.proj_matrix[0,0] = self.res_x * 0.5
            self.proj_matrix[1,1] = self.res_y * 0.5
            self.proj_matrix[3,0] = 0
            self.proj_matrix[3,1] = 0
            self.proj_matrix[3,3] = 1
        else:
            t = math.tan(self.fov)
            a = self.res_y / self.res_x
            self.proj_matrix[0,0] = 0.5 * self.res_x / t
            self.proj_matrix[1,1] = 0.5 * self.res_y / (a * t)
            self.proj_matrix[2,3] = 1
            self.proj_matrix[3,0] = 0
            self.proj_matrix[3,1] = 0

        return self.proj_matrix

    def get_camera_matrix(self):
        return Object3d.get_prs_matrix(-self.position, self.rotation.inverse(), vector3(1,1,1))
