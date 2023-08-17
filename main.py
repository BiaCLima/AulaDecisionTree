# Projeto realizado em sala de aula
# Aplicação de Modelos de Machine Learning
# Curso: Aplicações Informáticas para Ciência de Dados
# Professor: Tiago Cunha Reis, PhD
# Ipluso - Instituto Politécnico da lusofonia
# Autora: Bianca Costa

# 01 Bibliotecas necessárias
#! pip install scikit-learn
import matplotlib.pyplot as plt

# 02 Acessando a base de dados
# A base de dados usada está disponível em https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
from sklearn.datasets import load_iris
data_set = load_iris()

# Importação do algoritmo
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics

# ETAPA 1: Conjunto de dados e extração
X, Y = data_set.get('data'), data_set.get('target')
TARGET_NAMES = data_set.get('target_names')
FEATURE_NAMES = data_set.get('feature_names')

DESCRIPTION = data_set.get('DESCR') #Acessando a documentação técnica disponível no site scikit-learn

# Analisando a formados dados, se necessário
print(np.shape(X))
print(np.shape(Y))

# ETAPA 2: Split, para dividirmos os dados em conjuntos de treino e teste
split = 0.35

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=split)
# print(np.shape(X_train))

# ETAPA 3: Criação e treino do Algoritmo Decision Tree (Árvore de Decisão), utilizado para classificar
# os dados quando temos dados supervisionados (quando alguém(humano) o organizou e classificou)
model = DecisionTreeClassifier(max_depth=3)     # max_depth: definimos os nós da nossa árvore
model.fit(X_train, Y_train)                     # linha de ajuste/treino do nosso algoritmo

# Visualização da Árvore de Decisão
plt.figure()
plot_tree(model, filled=True, feature_names=FEATURE_NAMES,class_names=TARGET_NAMES)
plt.savefig('DecisionTree_iris')

# ETAPA 4: Validar/Testar o algoritmo, fazer previsões no conjunto de teste
P = model.predict(X_test)

# Matriz de confusão
cm = metrics.confusion_matrix(Y_test, P)
print("\nMatriz de Confusão:\n",cm)
