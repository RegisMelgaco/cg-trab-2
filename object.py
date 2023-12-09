import numpy as np
import math

class Object:
    def __init__(self, vectors, edges, color):
        self.vectors = vectors
        self.edges = edges
        self.color = color

    def move(self, position):
      t = np.array([
          [1, 0 , 0, position[0]],
          [0, 1 , 0, position[1]],
          [0, 0 , 1, position[2]],
          [0, 0 , 0, 1],
      ])

      self.vectors = np.matmul(t, self.vectors)

    def scale(self, s):
        t = np.array([
            [s[0], 0 , 0, 0],
            [0, s[1] , 0, 0],
            [0, 0 , s[2], 0],
            [0, 0 , 0, 1],
        ])

        self.vectors = np.matmul(t, self.vectors)

    def rotate_xy(self, angle):
        t = np.array([
            [math.cos(angle), -math.sin(angle) , 0, 0],
            [math.sin(angle), math.cos(angle) , 0, 0],
            [0, 0 , 1, 0],
            [0, 0 , 0, 1],
        ])

        self.vectors = np.matmul(t, self.vectors)

    def rotate_xz(self, angle):
        t = np.array([
            [1, 0 , 0, 0],
            [0, math.cos(angle), -math.sin(angle), 0],
            [0, math.sin(angle), math.cos(angle), 0],
            [0, 0 , 0, 1],
        ])

        self.vectors = np.matmul(t, self.vectors)