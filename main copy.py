from matplotlib import pyplot as plt
import numpy as np
import math
from cilinder import cilinder
from cone import cone
from sphere import sphere
from piramid_body import piramid_body
from cube import cube
from torus import torus


def move(vectors, pos):
    t = np.array([
        [1, 0 , 0, pos[0]],
        [0, 1 , 0, pos[1]],
        [0, 0 , 1, pos[2]],
        [0, 0 , 0, 1],
    ])

    return np.matmul(t, vectors)

def scale(vectors, s):
    t = np.array([
        [s[0], 0 , 0, 0],
        [0, s[1] , 0, 0],
        [0, 0 , s[2], 0],
        [0, 0 , 0, 1],
    ])

    return np.matmul(t, vectors)

def rotate_xy(vectors, angle):
    t = np.array([
        [math.cos(angle), -math.sin(angle) , 0, 0],
        [math.sin(angle), math.cos(angle) , 0, 0],
        [0, 0 , 1, 0],
        [0, 0 , 0, 1],
    ])

    return np.matmul(t, vectors)

def rotate_xz(vectors, angle):
    t = np.array([
        [1, 0 , 0, 0],
        [0, math.cos(angle), -math.sin(angle), 0],
        [0, math.sin(angle), math.cos(angle), 0],
        [0, 0 , 0, 1],
    ])

    return np.matmul(t, vectors)


class Object:
    def __init__(self, vectors, edges, color):
        self.vectors = vectors
        self.edges = edges
        self.color = color


def average_vectors(vectors):
    vs = vectors.transpose()
    acc = [0, 0, 0, 0]
    for v in vs:
        for i in range(len(v)):
            acc[i] += v[i]
    
    for i in range(len(vs[0])):
        acc[i] /= len(vs)

    return acc


# x = np.linspace(-10,10,10)
# y = np.linspace(-10,10,10)

# X,Y = np.meshgrid(x,y)
# Z=0*X

# subplot.plot_surface(X, Y, Z)

# vectors, edges, colors, centers = [], [], [], []
objects = []
centers = []

obj = cone(2, 4, 8)
obj.rotate_xz(math.pi/2)
obj.move((-7, 7, 0))
centers.append(average_vectors(obj.vectors))
objects.append(obj)

obj = piramid_body(4, 2, 2)
obj.rotate_xy(math.pi)
obj.move((-1, 1, 0))
centers.append(average_vectors(obj.vectors))
objects.append(obj)

obj = torus(4, 2, 8, 8)
obj.move((-7, 7, 7))
centers.append(average_vectors(obj.vectors))
objects.append(obj)

obj = sphere(2, 8, 8)
obj.move((3, 5, 2))
centers.append(average_vectors(obj.vectors))
objects.append(obj)

obj = cilinder(2, 3, 8)
obj.move((7, 3, 0))
centers.append(average_vectors(obj.vectors))
objects.append(obj)

obj = cube(5)
obj.scale((.9, .9, .9))
obj.move((6, 6, 0))
centers.append(average_vectors(obj.vectors))
objects.append(obj)

center = average_vectors(np.array(centers).transpose())
center = center[:3]
camera = np.array([-5,-5, 9])

up = [1,0,0]

n = (center - camera) / np.linalg.norm(center - camera)
print(np.linalg.norm(n))

u = up - ((np.dot(up, n) / np.linalg.norm(n) ** 2) * n)

v = np.cross(n, u)

t = np.array([
    [u[0], u[1], u[2], - camera[0]],
    [v[0], v[1], v[2], - camera[1]],
    [n[0], n[1], n[2], - camera[2]],
    [0, 0, 0, 1]
])


fig = plt.figure()
subplot = fig.add_subplot(111, projection='3d')

for obj in objects:
    for e in obj.edges:
        vs = np.matmul(t, obj.vectors)
        vs = vs.transpose()
        v1 = vs[e[0]]
        v2 = vs[e[1]]

        subplot.plot([v1[0], v2[0]], [v1[1], v2[1]], [v1[2], v2[2]], color=obj.color)

plt.grid(True)
plt.axis('equal')
plt.show()