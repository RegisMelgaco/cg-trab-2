from matplotlib import pyplot as plt
from cilinder import cilinder
from cone import cone
from sphere import sphere
from piramid_body import piramid_body
from cube import cube
from torus import torus


fig = plt.figure()
subplot = fig.add_subplot(111, projection='3d')

# vertices, edges = cilinder(2, 4, 8)

# vertices, edges = cone(2, 4, 8)

# vertices, edges = sphere(2, 4, 8)

# vertices, edges = piramid_body(8, 4, 2)

# vertices, edges = cube(2)

vertices, edges = torus(4, 2, 16, 16)

for e in edges:
    v1 = vertices[e[0]]
    v2 = vertices[e[1]]

    subplot.plot([v1[0], v2[0]], [v1[1], v2[1]], [v1[2], v2[2]], color='blue')

plt.grid(True)
plt.axis('equal')
plt.show()