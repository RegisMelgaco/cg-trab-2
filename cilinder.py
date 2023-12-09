
import math


def cilinder(radius, circle_count, circle_res):
    vertices, edges = [], []

    height = 2*radius
    h = height/circle_count

    # comptu dos circulos
    steps = [(c*2*math.pi)/circle_res for c in range(circle_res)]
    for i in range(circle_count):
        edges += [[c+len(vertices), c+len(vertices)+1] for c in range(circle_res-1)]
        edges += [[len(vertices), len(vertices)+circle_res-1]]
        vertices += [
            [math.sin(s) * radius,
             math.cos(s) * radius,
             h*i,
             1
             ] for s in steps]
    
    # conectar verticalmente os circulos
    edges += [[i*circle_res, (i+1)*circle_res] for i in range(circle_count-1)]

    return vertices, edges

