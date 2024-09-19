# A biblioteca socket interage com a api socket do SO, que abre e fecha conexão
import socket

# Não confundir com a biblioteca OS. A Biblioteca Sys fornece acesso a algumas variáveis e funções que possuem forte interação com o interpretador
import sys

def main():
    # Tentando uma conexão TCP

    try:
    
        # AF_INET parametro que defini o protocolo IP usado
        # SOCK_STREAM parâmetro que define o protocolo
        # Parametro 0 defini otipo do protocolo, sendo este como TCP
        
        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)

    except socket.error as e:  

        print("A conexão falhou")
        print("Erro: {}".format(e))

        sys.exit()

    print("socket criado!")

    host_alvo = input("digite o Ip a ser conectado")
    porta_alvo = input("digite a porta a ser conectada")

    try:
        s.connect((host_alvo, int(porta_alvo)))

        print("conecado ao cliente tcp")

        s.shutdown(2)
    
    except socket.error as e:

        print("a conexao falhou")
        print("erro: {}".format(e))

        sys.exit()

if (__name__ == "__main__"):
    main()