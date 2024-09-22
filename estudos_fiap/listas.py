#primeiro importamos o módulo sys
import sys
#agora vamos criar uma lista vazia
lista = ["a","b","c",'d','e']
#E verificar o tamanho
print("O objeto lista é do tipo {} e tem {} bytes".format(type(lista), sys.getsizeof(lista)))

print(lista.index('f'))