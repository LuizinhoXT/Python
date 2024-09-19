import ctypes

atributo = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW("teste.txt", atributo)

if retorno:
    print("Ocultado")
else:
    print("nao ocultado")
