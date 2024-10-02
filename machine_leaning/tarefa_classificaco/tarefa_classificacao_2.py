import pandas as pd 
from sklearn.metrics import accuracy_score


# Base de dados utilizada no estudo
uri='https://gist.githubusercontent.com/guilhermesilveira/2d2efa37d66b6c84a722ea627a897ced/raw/10968b997d885cbded1c92938c7a9912ba41c615/tracking.csv'

# todos os dados do CSV
dados = pd.read_csv(uri)

# Mapa chave : valor para alterar os nomes das colunas do conjunto
mapa = {
    'home' : 'pagina_inicial',
    'how_it_works' : 'como_funciona',
    'contact' : 'contato',
    'bought' : 'comprou'
}

dados = dados.rename(columns=mapa)


# print(f"Colunas: {dados.columns}, Tamanho: {dados.shape}" )
# Output: Colunas: ['pagina_inicial', 'como_funciona', 'contato', 'comprou'] | Tamanho: (99, 4)



# Separando as variáveis X e Y do conjunto principal

x = dados[['pagina_inicial', 'como_funciona', 'contato']]
y = dados['comprou']


# Dados para treino com 75 elementos
treino_x = x[:75]
treino_y = y[:75]

# Dados para teste com 24 elemtnos
teste_x = x[75:]
teste_y = y[75:]

# Função para instanciar e treinar o modelo com os dados de treino
def treino(vars_x, vars_y):
    from sklearn.svm import LinearSVC

    md = LinearSVC()
    md.fit(vars_x, vars_y)

    return md

# Modelo instanciado e treinado com as variáveis teste x e y, sendo assim, o algotirmo consegue entender como o conjunto de features de x se realciona com y.
modelo_treinado = treino(treino_x, treino_y)

# A partir do modelo treinado é possível predizer quais serão os valores de y.
predicao = modelo_treinado.predict(teste_x)

# Medição da acurácia do modelo comparando os valores verdadeiros com os valores da predicao do modelo.
acuracia = accuracy_score(teste_y, predicao) * 100

print("a curácia foi %.2f%%" % acuracia)
