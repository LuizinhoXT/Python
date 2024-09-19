import socket

# Criando o socket do servidor

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

print("socket criado")

host = "localhost"
porta = 5432

s.bind((host, porta))

count = 0


mensagem = "\nservidor: cliente conectado com sucesso"

while 1 :
    dados, end = s.recvfrom(4896)

    # entra no if se e apenas se possui dados
    
    if dados:
        print("mensagem recebida! \n dados: {} ".format(dados))
        count = count + 1
        print('qty conexoes ao server' + str(count))
        s.sendto((mensagem.encode()), end)



