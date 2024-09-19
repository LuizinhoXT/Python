import random
import string

tamanho = 16

# defini os caracteres que serão usados na senha, podendo escolher entre diversas combinações de caracteres

chare = string.ascii_letters + string.digits + "!@#$%&*?_"

# os.urandom

rnd = random.SystemRandom() 

print("".join(rnd.choice(chare) for i in range(tamanho)))
