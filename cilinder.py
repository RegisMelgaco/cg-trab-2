import numpy as np
import math
from object import Object


def cilinder(radius, circle_count, circle_res):
    vectors, edges = [], []

    height = 2*radius
    h = height/circle_count

    # comptu dos circulos
    steps = [(c*2*math.pi)/circle_res for c in range(circle_res)]
    for i in range(circle_count):
        edges += [[c+len(vectors), c+len(vectors)+1] for c in range(circle_res-1)]
        edges += [[len(vectors), len(vectors)+circle_res-1]]
        vectors += [
            [math.sin(s) * radius,
             math.cos(s) * radius,
             h*i,
             1
             ] for s in steps]
    
    # conectar verticalmente os circulos
    edges += [[i*circle_res, (i+1)*circle_res] for i in range(circle_count-1)]


    return Object(np.array(vectors).transpose(), edges, 'blue')