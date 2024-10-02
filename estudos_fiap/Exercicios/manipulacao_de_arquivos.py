# Abrindo arquivo
arquivo1 = open("C:/Users/luizf/Workspace/arquivos/arquivo_de_texto.txt", "r")

# lendo o conteúdo
for line in arquivo1:
    print('\n',arquivo1.readline(), "\n")

# Conteúdo
texto = "sobreescrevendo arquivo criado em tempo de execução..."

# Abrindo arquivo
arquivo2 = open("C:/Users/luizf/Workspace/arquivos/arquivo_de_texto_criado_em_exe.txt", "w")

# Ecrevendo no arquivo
arquivo2.write(texto)

# Reabrindo em modo de leitura
arquivo2 = open("C:/Users/luizf/Workspace/arquivos/arquivo_de_texto_criado_em_exe.txt", "r")

print("AROOZ E FEIJAO")

# lendo arquivo criado em tempo de execução
print(arquivo2.readline())

# ferchando o arquivo
arquivo1.close()
arquivo2.close()

------------
