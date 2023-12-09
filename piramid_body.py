import numpy as np


def piramid_body(base, top, height):
    vertices, edges = [], []

    # base
    vs = np.array([
        [0, 0, 0, 1],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [1, 0, 0, 1]])
    t = np.array([
        [base, 0, 0, 0],
        [0, base, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])
    vertices += np.matmul(t, vs.transpose()).transpose().tolist()

    edges += [[i, i+1] for i in range(3)]
    edges += [[0, 3]]

    # top
    offset = (base-top)/2
    v = np.array([
        [0, 0, 1, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 0, 1, 1]]).transpose()
    t = np.array([
        [top, 0, 0, offset],
        [0, top, 0, offset],
        [0, 0, height, 0],
        [0, 0, 0, 1]])
    vertices += np.matmul(t, v).transpose().tolist()

    edges += [[i, i+1] for i in range(4, 7)]
    edges += [[4, 7]]

    # conectando topo e base
    edges += [[i, i+4] for i in range(4)]


    return vertices, edges

