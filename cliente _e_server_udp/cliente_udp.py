import socket

# S é um Objeto de conexão

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("cliente socket criado \n")

# host e porta é o endereço do servidor
# host é equivalente a google.com.br
# porta é equivalente a 80 ou 8080

host = "localhost"
porta = 5466 

# msg é o dado enviado para o servidor. Nesse caso, é um dado NAO estruturado

msg = "salve servidor, firmeza"

def msg_to_server():

    a = input("digite a mensagem para enviar ao servidor")

    return a


try:
    print("cliente: " + msg)

    # encode irá envelopar a mensagem em pacotes UDP e direcionando para o servidor
    # o servidor que está escutando de maneira contínua está definido no arquivo: server_udp.py

    s.sendto(msg.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4896)

    dados = dados.decode()

    print("cliente" + dados)
finally:
    # print("cliente : fechando a conexão")

    while 1:
    
        var = input("digite a mensagem para enviar ao servidor")

        s.sendto(var.encode(), (host, 5432))


    
    s.close()