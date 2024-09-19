import pandas as pd
import math
import matplotlib.pyplot as plt

df = pd.read_excel("Python\Análise_exploratória\AdventureWorks.xlsx")

# Exibe os dados armazenados no dataframe
#print(df.head())

# Exibindo os tipos de dados de cada campo

#print(df.dtypes)

# Exibindo a quantidade de linhas x colunas do dataframe

#print("\n",df.shape)



# Qual é a receita total?

soma_vendas = df["Valor Venda"].sum()

print(f"A Receita total é R$ {math.ceil(soma_vendas)}")

# Qual é o custo total?

df["Custo"] = df["Custo Unitário"] * df["Quantidade"]

soma_custo = df["Custo"].sum()

print(f"O Custo total é de R$ {math.ceil(soma_custo)}")

# Qual é o lucro total?
# É preciso calcular a receita e o custo para calcular o lucro

df["Lucro"] = df["Valor Venda"] - df["Custo"]

lucro_total = df["Lucro"].sum()

print(f"O lucro total é de R$ {math.ceil(lucro_total)}")

# Qual é o Lead Time do venda par envio de cada produto?
# É preciso criar uma nova coluna que subtraia a data de venda e a data de envio

df["Tempo Para Envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

# qual é média de tempo de envio por marca?
# é preciso grupar pormarca com groupby e usar função mean()

# Lucro por ano e por marca?
# É preciso por dois parâmetros: ano e marca. Por fim, precisa realizar soma.

pd.options.display.float_format = "{:20,.2f}".format

print(df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum().reset_index())

# Qual o total de produtos vendidos?

print(df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)) 

# Com Gráficos

print(df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False).plot.barh(title="Total Produtos Vendidos"))
plt.xlabel("Total")
plt.ylabel("Produto") 

# qual o lucro por ano?

df.groupby(df["Data Venda"].dt.year)["Lucro"].sum().plot.bar(title="Lucro Por Ano")
plt.xlabel("Ano")
plt.ylabel("Receita")

# Qual o lucro em 2009

df_2009 = df[df["Data Venda"].dt.year == 2009]


# Qual o lucro por mês no ano de 2009

print(df_2009.head())

df_2009.groupby(df_2009["Data Venda"].dt.month)["Lucro"].sum().plot(title= "Lucro x Ano")
plt.xlabel("Mês")
plt.ylabel("Lucro")

# Qual o lucro por marca?

df_2009.groupby("Marca")["Lucro"].sum().plot.bar(title="Lucro x Mrca")
plt.xlabel("Lucro")
plt.ylabel("Marca")
plt.xticks(rotation="horizontal")

# Lucro por classe?

df_2009.groupby("Classe")["Lucro"].sum().plot.bar(title="Lucro x classe")

# Algumas análises estatisticas

print(df["Tempo Para Envio"].describe())

plt.boxplot(df["Tempo Para Envio"])

# Média de envio dos itens
# Desvio padrão 
# Q1 Quart 25% enviados em x dias
# Q2 Quart 50% enviados em x dias
# Q3 Quart 75% enviados em x dias
# max 20.00
# Quantidade minima de tempo para envio (em dias) é um limite inferior
# Quantidade máxima de tempo para envio (em dias) é um limite superior
# Um valor muito alto é um outlier que é um ponto fora da curva e que pode influenciar os  dados, também chamado de ponto influente

plt.hist(df["Tempo Para Envio"])

df["Tempo Para Envio"].min()

df["Tempo Para Envio"].max()

outlier = df[df["Tempo Para Envio"]== 20]