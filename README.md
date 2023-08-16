# Aula: DecisionTree

- Projeto realizado em sala de aula
- Aplicação de Modelos de Machine Learning
- Curso: Aplicações Informáticas para Ciência de Dados
- Professor: Tiago Cunha Reis, PhD
- Ipluso - Instituto Politécnico da Lusofonia
- Data: 28/03/2023
- Autora: Bianca Lima

![Badge Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=GREEN&style=for-the-badge)

## Descrição do Projeto

Projeto desenvolvido em sala de aula para estudo de Algoritmos de Machine Learning, neste caso de Árvore de Decisão.  
Tem como objetivo desenvolver as habilididades de análise do Algoritmos e das ferramentas de programação.  

 1. Introdução
    - O algoritmo de árvore de decisão cria vários pontos de decisão, que são chamados de 'nós', que nos retorna o resultado da decisão para então seguir por um ou outro caminho, ou seja, é um algoritmo de classificação.
    - Durante esse projecto classificaremos os tipos de planta.
        
 2. Bibliotecas
    - Neste projeto, foram utilizadas três bibliotecas importantes: matplotlib, scikit-learn e numpy.  A biblioteca matplotlib foi empregada para a visualização gráfica dos dados e resultados, enquanto a scikit-learn foi usada para criar e treinar o modelo de Árvore de Decisão.

 3. Dados
    - Foi utilizado o conjunto de dados da íris, disponibilizado no site scikit-learn.org (https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html).
    - Esse conjunto de dados consistem em 3 tipos diferentes de comprimento de pétala e sépala de íris (Setosa, Versicolour e Virginica), armazenados em um numpy.ndarray de 150 x 4.

As linhas são as amostras e as colunas são: Comprimento da Sépala, Largura da Sépala, Comprimento da Pétala e Largura da Pétala.

 4. Análise
    -  Para compreender melhor os dados gerados, realizou-se uma análise exploratória com uma representação gráfica por meio de um histograma. Essa visualização permite identificar a distribuição dos dados e obter insights iniciais sobre a relação entre a idade e a pressão arterial em nosso conjunto de dados fictícios:

     ![Image](Histograms.png)

 6. Modelo de Regressão Linear
    - Desenvolvimento do modelo de Regressão Linear com uso da biblioteca scikit-learn.
    - O Algoritmo de Regressão Linear é um método supervisionado de aprendizagem que tem como objetivo modelar a relação entre uma variável dependente e uma ou mais variáveis independentes, estabelecimento a melhor relação entre elas.
   
 6. Previsão
    - O modelo utiliza os dados para identificar a relação linear entre idade e pressão arterial e, em seguida, faz previsões para outras idades com base nessa relação.
    - Foi realizada a previsão da pressão arterial em relação a idade dos dados fictícios que foram gerado, com uso da biblioteca scikit-learn. Portanto, essas previsões são apenas ilustrativas e não devem ser consideradas como resultados precisos para dados reais.
     
    - Os resultados a seguir são um exemplo das previsões da pressão arterial para diferentes idades usando o modelo de Regressão Linear desenvolvido neste projeto.  

   Para 20.0 anos, previsão = 114.02 mmHg  
   Para 35.0 anos, previsão = 124.65 mmHg  
   Para 50.0 anos, previsão = 135.28 mmHg  
   Para 65.0 anos, previsão = 145.91 mmHg  
   Para 80.0 anos, previsão = 156.55 mmHg  

 8. Representação gráfica
    - Foi realizada a representação gráfica da Regressão Linear entre a idade e a pressão arterial, por meio um Scatter.

     ![Image](Scatter.png)
     
## Acesso ao Projeto

- Você pode acessar o código fonte do projeto inicial ou baixá-lo.

## Tecnologia usada
 
 - Python
 - PyCharm
