import math
import numpy as np
from object import Object


def sphere(radius, circle_count, circle_res):
    vectors, edges = [], []

    steps = [(c*2*math.pi)/circle_res for c in range(circle_res)]
    for i in range(circle_count+1):
        edges += [[c+len(vectors), c+len(vectors)+1] for c in range(circle_res-1)]
        edges += [[len(vectors), len(vectors)+circle_res-1]]

        vs = np.array([
            [math.sin(s) * radius,
             0,
             math.cos(s) * radius,
             1] for s in steps])
        
        c = math.pi/circle_count
        t = np.array([
            [math.cos(i*c), -math.sin(i*c), 0, 0],
            [math.sin(i*c), math.cos(i*c), 0, 0],
            [0,0,1,0],
            [0,0,0,1],
            ])
        vs = np.matmul(t, vs.transpose()).transpose()
        
        vectors += vs.tolist()
    
    for i in range(circle_count):
        edges += [[j+(circle_res*i), j+(circle_res*(i+1))] for j in range(1, circle_res)]


    return Object(np.array(vectors).transpose(), edges, 'pink')