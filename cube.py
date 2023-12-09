import numpy as np


def cube(side):
    v = np.array([
        [0, 0, 0, 1],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [1, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 0, 1, 1]]).transpose()
    
    t = np.array([
        [side, 0, 0, 0],
        [0, side, 0, 0],
        [0, 0, side, 0],
        [0, 0, 0, 1]]).transpose()
    
    v = np.matmul(t, v)

    edges = [[i, i+1] for i in range(3)] # conectando base
    edges += [[i, i+1] for i in range(4, 7)] # conectando topo
    edges += [[i, i+4] for i in range(4)] # conectando base ao topo
    edges += [[0, 3], [4, 7]] # conectanto começos a fins

    return v, edges