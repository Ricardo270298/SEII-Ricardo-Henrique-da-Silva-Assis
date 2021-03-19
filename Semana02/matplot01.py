import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [0,1,2,3,4]
y = [0,2,4,6,8]

# Arruma o tamanho do grafico (dpi specifies pixels per inch. When saving probably should use 300 if possible)
plt.figure(figsize=(8,5), dpi=100)

plt.plot(x,y, 'b^--', label='2x')

## Line 2

# Seleciona o intervalo
x2 = np.arange(0,4.5,0.5)

# Plota parte do grafico como linhas
plt.plot(x2[:6], x2[:6]**2, 'r', label='X^2')

# Plota o resto do grafico como traços
plt.plot(x2[5:], x2[5:]**2, 'r--')

# Adiciona o titulo (specifica os parametros da font com fontdict)
plt.title('Our First Graph!', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})

# X and Y labels
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# X, Y axis Tickmarks 
plt.xticks([0,1,2,3,4,])
#plt.yticks([0,2,4,6,8,10])

# Legenda
plt.legend()

# Salva a figura(dpi 300 is good when saving so graph has high resolution)
plt.savefig('mygraph.png', dpi=300)

# Show plot
plt.show()
