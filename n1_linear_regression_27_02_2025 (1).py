# -*- coding: utf-8 -*-
"""N1_Linear_Regression_27_02_2025.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fPmplYyvaHaVTpJlVsrIVd1NC_-ThVpf

<a rel="license" href="https://faculdadesalvadorarena.org.br/"><img alt="FESA" style="border-width:0" src="https://faculdadesalvadorarena.org.br/wp-content/uploads/2022/07/logo_fesa.png" /></a><br />
**FESA - Eletiva II (2025.1)** <br/>

Aluno(a): Rodrigo Moro Batalha <br/>
Data: 08/03/2025 <br/>
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
plt.rcParams.update(params)

"""# Regressão Linear Simples

## 1. Explorando o Dataset

Dataset fictício criado para explicar regressão linear simples. <br/>
https://grouplens.org/datasets/movielens/

O dataset ele nos mostra como cada individuo avaliou
um filme, demonstrando o título, ano de lançamento,
gênero e um comentário(tag) sobre o mesmo.

### 1.1. Importando o Dataset

Importar as tabelas de referencia para a manipulação
"""

df1 = pd.read_csv('/content/links.csv')
df2 = pd.read_csv('/content/movies.csv')
df3 = pd.read_csv('/content/ratings.csv')
df4 = pd.read_csv('/content/tags.csv')



"""Com a função .head(), obtemos os primeiros atributos da tabela

no caso da tabela Links, Mostra parâmetros de sites de recomendações, possuindo os atributos de movieId, imdbId e tmdbId
"""

df1.head()

"""Na tabela movies, Cada linha descreve um filme, onde temos os atributos: movieId, title, genres"""

df2.head()

"""Na tabela ratings cada linha descreve a avalição de um filme
por 1 usuario, possuindo os atributos UserId, MovieId, ratings e timestamp
"""

df3.head()

"""e na ultima tabela (Tags)  mostra como cada usuário identificou um filme, possuindo os atributos: userId, MovieId, tag e timestamp"""

df4.head()

"""### 1.2. Informações básicas do dataset

Para sabermos um pouco mais dos dataframes que temos, buscamos o total de linhas e colunas correspondentes de cada uma
"""

print(f'O dataset possui {df1.shape[0]} exemplos/amostras/linhas e {df1.shape[1]} atributos/variáveis/colunas.')

print(f'O dataset possui {df2.shape[0]} exemplos/amostras/linhas e {df2.shape[1]} atributos/variáveis/colunas.')

print(f'O dataset possui {df3.shape[0]} exemplos/amostras/linhas e {df3.shape[1]} atributos/variáveis/colunas.')

print(f'O dataset possui {df4.shape[0]} exemplos/amostras/linhas e {df4.shape[1]} atributos/variáveis/colunas.')

"""Com o .info() conseguimos saber quais são os tipos de atributos, ou seja, qual e o tipo de cada variável/atributo"""

df1.info()

"""Assim podemos observar os atributos/colunas e seus tipos como:

movieID: int 64

imdbId: int 64

tmbdId: float 64

Como podemos observar, o atributo tmdbId, da tabela Links, possui alguns valores incompletos alem de possuir o tipo de dado Float, que indica numeros com virgula, o que não se enquadra muito.
Portanto vamos ajeitar ...
"""

df1['tmdbId'].fillna(0)
df1['tmdbId'] = df1['tmdbId'].astype(int)
df1.info()

"""Agorta que os valores foram ajustados vamos para a próxima tabela

A tabela de Movies está boa
"""

df2.info()

"""Possuindo os seguintes aspectos:

movieId: int 64

o title: Object

o genres: object
"""

df3.info()

"""A tabela ratings está boa também, e possui os seguintes detalhes:
userId: int64

movieId: int 64

o rating: float 64

o timestamp: int 64

E a ultima tabela de Tags está coerente também
"""

df4.info()

"""Possuindo os seguintes aspectos:

userId: int 64

movieId: int 64

tag: object

timestamp: int 64

UM POUCO MAIS DE DADOS DE CADA DATAFRAME

### 1.3. Estatísticas Descritivas
"""

df1.describe()

df2.describe()

df3.describe()

df4.describe()