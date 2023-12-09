from matplotlib import pyplot as plt
import numpy as np
import math
from cilinder import cilinder
from cone import cone
from sphere import sphere
from piramid_body import piramid_body
from cube import cube
from torus import torus


def average_vectors(vectors):
    vs = vectors.transpose()
    acc = [0, 0, 0, 0]
    for v in vs:
        for i in range(len(v)):
            acc[i] += v[i]
    
    for i in range(len(vs[0])):
        acc[i] /= len(vs)

    return acc


class World:
    objects = []
    eye = np.array([-5,-5, 9])

    def plot_world_sys(self):
        fig = plt.figure()
        subplot = fig.add_subplot(111, projection='3d')

        centers = [average_vectors(obj.vectors) for obj in self.objects]
        at = average_vectors(np.array(centers).transpose())

        subplot.plot([self.eye[0], at[0]], [self.eye[1], at[1]], [self.eye[2], at[2]], color='orange')

        for obj in self.objects:
            for e in obj.edges:
                vs = obj.vectors.transpose()
                v1 = vs[e[0]]
                v2 = vs[e[1]]

                subplot.plot([v1[0], v2[0]], [v1[1], v2[1]], [v1[2], v2[2]], color=obj.color)

        plt.grid(True)
        plt.axis('equal')
        plt.show()

    def plot_camera_sys(self):
        fig = plt.figure()
        subplot = fig.add_subplot(111, projection='3d')

        centers = [average_vectors(obj.vectors) for obj in self.objects]
        at = average_vectors(np.array(centers).transpose())[:3]

        up = [1,0,0]

        n = (at - self.eye) / np.linalg.norm(at - self.eye)

        u = up - ((np.dot(up, n) / np.linalg.norm(n) ** 2) * n)

        v = np.cross(n, u)

        t = np.array([
            [u[0], u[1], u[2], - self.eye[0]],
            [v[0], v[1], v[2], - self.eye[1]],
            [n[0], n[1], n[2], - self.eye[2]],
            [0, 0, 0, 1]
        ])

        for obj in self.objects:
            for e in obj.edges:
                vs = np.matmul(t, obj.vectors)
                vs = vs.transpose()
                v1 = vs[e[0]]
                v2 = vs[e[1]]

                subplot.plot([v1[0], v2[0]], [v1[1], v2[1]], [v1[2], v2[2]], color=obj.color)

        plt.grid(True)
        plt.axis('equal')
        plt.show()


if __name__ == '__main__':
    w = World()

    obj = cone(2, 4, 8)
    obj.rotate_xz(math.pi/2)
    obj.move((-7, 7, 0))
    w.objects.append(obj)

    obj = piramid_body(4, 2, 2)
    obj.rotate_xy(math.pi)
    obj.move((-1, 1, 0))
    w.objects.append(obj)

    obj = torus(4, 2, 8, 8)
    obj.move((-7, 7, 7))
    w.objects.append(obj)

    obj = sphere(2, 8, 8)
    obj.move((3, 5, 2))
    w.objects.append(obj)

    obj = cilinder(2, 3, 8)
    obj.move((7, 3, 0))
    w.objects.append(obj)

    obj = cube(5)
    obj.scale((.9, .9, .9))
    obj.move((6, 6, 0))
    w.objects.append(obj)

    w.eye = np.array([-5,-5, 9])

    w.plot_world_sys()
    w.plot_camera_sys()