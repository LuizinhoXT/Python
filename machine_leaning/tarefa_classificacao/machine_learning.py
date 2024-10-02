# import
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score



# Tarefa de classificação: Padeiro ou Programador?

# Features

# Escreve código? Sim ou Não
# Amassa pão? Sim ou Não
# Gosta de matemática? SIm ou não
# Vendo Pão? Sim ou não

# Definição de features
pdr1 = [0, 1, 0, 1]
pdr2 = [1, 1, 0, 1]
pdr3 = [0, 1, 1, 1]

pgr1 = [1, 1, 0, 0]
pgr2 = [1, 0, 1, 1]
pgr3 = [1, 0, 0, 0]

# Agrupando dados
dados = [pdr1,pdr2,pdr3,pgr1,pgr2,pgr3]

# padeiro => 1; programador => 0
classes = [1,1,1,0,0,0]

# Intanciação do modelo
model = LinearSVC()

# Aprendizado
model.fit(dados, classes)

# Profissao misteriosa
ps_mist1 = [1, 1, 1, 1] # y = 0
ps_mist2 = [1, 0, 0, 1] # y = 1
ps_mist3 = [0, 1, 1, 0] # y = 0
ps_mist4 = [1, 1, 0, 1] # y = 1


# testes para Mmquina
testes = [ps_mist1,ps_mist2,ps_mist3,ps_mist4]

# Valores verdadeiros
val_true = [0,1,0,1]

# Predição máquina
prd_machine = model.predict(testes)

# Quantidade de valores corretos
val_corretos = ((prd_machine == val_true).sum())

# Tamanho tetes
tam_testes = len(testes)

# Taxa de acerto = (qty_testes_corretos / tamanho_testes)
tax_acerto = (val_corretos / tam_testes * 100), "%"

# Acuracy Score
acc_score = accuracy_score(val_true, prd_machine)