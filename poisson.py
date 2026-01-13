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

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
  "normal": random.normal(loc=50, scale=7, size=1000),
  "poisson": random.poisson(lam=50, size=1000)
}

sns.displot(data, kind="kde")

plt.show()
"""