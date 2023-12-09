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


def add_object(word_vectors, word_edges, obj_vectors, obj_edges):
    c = len(word_vectors.transpose())
    for i in range(len(obj_edges)):
        obj_edges[i][0] += c
        obj_edges[i][1] += c

    return np.array(word_vectors.transpose().tolist() + obj_vectors.transpose().tolist()).transpose(), word_edges + obj_edges

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

fig = plt.figure()
subplot = fig.add_subplot(111, projection='3d')

# subplot.plot_surface(X, Y, Z)

vectors, edges, centers = np.array([]), [], []

vs, es = cone(2, 4, 8)
vs = rotate_xz(vs, math.pi/2)
vs = move(vs, (-7, 7, 0))
centers.append(average_vectors(vs))
vectors, edges = add_object(vectors, edges, vs, es)

vs, es = piramid_body(4, 2, 2)
vs = rotate_xy(vs, math.pi)
vs = move(vs, (-1, 1, 0))
centers.append(average_vectors(vs))
vectors, edges = add_object(vectors, edges, vs, es)

vs, es = torus(4, 2, 8, 8)
vs = move(vs, (-7, 7, 7))
centers.append(average_vectors(vs))
vectors, edges = add_object(vectors, edges, vs, es)

vs, es = sphere(2, 8, 8)
vs = move(vs, (3, 5, 2))
centers.append(average_vectors(vs))
vectors, edges = add_object(vectors, edges, vs, es)

vs, es = cilinder(2, 3, 8)
vs = move(vs, (7, 3, 0))
centers.append(average_vectors(vs))
vectors, edges = add_object(vectors, edges, vs, es)

vs, es = cube(5)
vs = scale(vs, (.9, .9, .9))
vs = move(vs, (6, 6, 0))
centers.append(average_vectors(vs))
vectors, edges = add_object(vectors, edges, vs, es)

center = average_vectors(np.array(centers).transpose())
camera = [-5,-5, 9]

n = np.array(center[:3]) - np.array(camera)

up = [0,0,1]

u = np.cross(up, n)
v = np.cross(n, u)

n = np.divide(n, np.linalg.norm(n))
u = np.divide(u, np.linalg.norm(u))
v = np.divide(v, np.linalg.norm(v))

print(f'n={n};\nu={u};\nv={v};')

subplot.quiver(camera[0], camera[1], camera[2], n[0], n[1], n[2])
# subplot.arrow(camera, n, color='red')

# V = np.matrix([
#     [u[0], u[1], u[2], - camera[0] * u[0] - camera[1] * u[1] - camera[2] * u[2]],
#     [v[0], v[1], v[2], - camera[0] * v[0] - camera[1] * v[1] - camera[2] * v[2]],
#     [n[0], n[1], n[2], - camera[0] * n[0] - camera[1] * n[1] - camera[2] * n[2]],
#     [0, 0, 0, 1]
# ])

# vectors = np.matmul(V, np.array(vectors).transpose()).transpose()

vectors = vectors.transpose()

for e in edges:
    v1 = vectors[e[0]]
    v2 = vectors[e[1]]

    subplot.plot([v1[0], v2[0]], [v1[1], v2[1]], [v1[2], v2[2]], color='blue')


plt.grid(True)
plt.axis('equal')
plt.show()