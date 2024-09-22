import csv

# dados de vendas ficticios gerados com chatGPT 
vendas = [
    
['6','Jaqueta de Couro','1','299.90','2024-09-06'],
['7','Sapatilha','2','89.90','2024-09-07'],
['8','Camisa Social','1','79.90','2024-09-08'],
['9','Shorts de Praia','3','39.90','2024-09-09'],
['10','Cinto de Couro','2','59.90','2024-09-10'],
['11','Tênis Casual','1','159.90','2024-09-11'],
['12','Mochila Escolar','1','69.90','2024-09-12'],
['13','Vestido Floral','1','129.90','2024-09-13'],
['14','Óculos de Sol','1','99.90','2024-09-14'],
['15','Boné Esportivo','2','39.90','2024-09-15'],
['16','Relógio Analógico','1','199.90','2024-09-16'],
['17','Blusa de Frio','2','149.90','2024-09-17'],
['18','Saia Midi','1','89.90','2024-09-18'],
['19','Bermuda Cargo','1','79.90','2024-09-19'],
['20','Tênis de Corrida','1','249.90','2024-09-20'],
['21','Casaco de Inverno','1','349.90','2024-09-21']

]


with open('C:/users/luizf/Workspace/Arquivos/vendas.csv', mode = 'a') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv,delimiter=',')
    for linha in vendas:
        escritor_csv.writerow(linha)
