"""
Estive a procurar soluções para gerar e visualizar distribuições de Poisson em Python. Aqui estão dois exemplos que encontrei úteis:    
1)

Geração de Amostras de uma Distribuição de Poisson

import numpy as np

lambda_ = 3  # Taxa média
tamanho = 1000 # Quantas amostras gerar

# Gera 1000 amostras de uma distribuição de Poisson com lambda=3
dados_poisson = np.random.poisson(lambda_, tamanho)

# Exibe as primeiras amostras
print("Primeiras 10 amostras:", dados_poisson[:10])

# Média e variância das amostras (devem ser próximas de lambda)
print(f"Média das amostras: {np.mean(dados_poisson):.2f}")
print(f"Variância das amostras: {np.var(dados_poisson):.2f}")

2)Visualização da Distribuição de Poisson vs Normal

"""
import numpy
import matplotlib.pyplot as plt

data = {
  "normal": numpy.random.normal(loc=50, scale=7, size=10000),
  "poisson": numpy.random.poisson(lam=50, size=1000)
}

counts, bin_edges, _ =  plt.hist(data["normal"], bins=50)
# Compute bin centers
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

# Step 1: downsample to 25 points for smoothing
downsample_step = 3
x_ds = bin_centers[::downsample_step]
y_ds = counts[::downsample_step]

# Step 2: interpolate back to 50 points (align with original bins)
x = bin_centers
y = numpy.interp(x, x_ds, y_ds)

# Step 3: ensure the maximum bin is preserved
max_idx = numpy.argmax(counts)
y[max_idx] = counts[max_idx]

plt.plot(x,y)
#plt.hist(data["poisson"], bins=50)

plt.show()