import hashlib


arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new("ripemd160")

hash1.update(open(arquivo1, 'rb').read())

print("a")

hash2 = hashlib.new("ripemd160")

hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print( "os arquivos são diferentes")
else: 
    print("Arquivos iguais")

