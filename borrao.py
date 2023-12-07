from matplotlib import pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot([0, 1], [0, 1], [0,1], color='blue')
plt.grid(True)  # Ativa a grade de fundo
plt.show()  # Mostra o gráfico