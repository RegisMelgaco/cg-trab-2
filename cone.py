import math


def cone(radius, circle_count, circle_res):
    vertices, edges = [], []

    height = 3*radius
    h = height/circle_count
    r = radius/circle_count

    steps = [(c*2*math.pi)/circle_res for c in range(circle_res)]
    for i in range(circle_count):
        edges += [[c+len(vertices), c+len(vertices)+1] for c in range(circle_res-1)]
        edges += [[len(vertices), len(vertices)+circle_res-1]]
        vertices += [
            [math.sin(s) * (radius - (r*i)),
             math.cos(s) * (radius - (r*i)),
             h*i
             ] for s in steps]
    
    vertices += [[0, 0, height]]
    edges += [[i*circle_res, (i+1)*circle_res] for i in range(circle_count)]

    return vertices, edges