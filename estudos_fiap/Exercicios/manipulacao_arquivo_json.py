# Aqruivo vasio criado com o comendo : echo > manipulacao_arquivo_json.py

#importando o módulo json
import json

#criando um dicionário para usarmos como exemplo
contatos = {
    "Luiz farias":
        {"Celular":"897123",
         "Email":"luiz@arroz.com.br"},
    "Amanda Santos":
        {"Celular":"231567",
         "Email":"amanda@batata.com.br"}     
}

#convertendo o dicionário para uma string o formato json
final = json.dumps(contatos, indent=4)

with open("C:/users/luizf/Workspace/Arquivos/contatos.json", "w") as arquivo_json:

    #escrevendo o JSON dentro do arquivo
    arquivo_json.write(final)

    #fechando arquivo como boa prática
    arquivo_json.close()



  #exibindo a string convertida
    print(final)