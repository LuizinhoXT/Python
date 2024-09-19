class Animal():
    def __init__(self,nome, num_patas):
        self.num_patas = num_patas
        self.nome = nome
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


      

class Mamifero(Animal):
    def __init__(self, cor_do_pelo, **kw):
        super().__init__(**kw)
        self.cor_do_pelo = cor_do_pelo
    pass

class Ave(Animal):
    def __init__(self, cor_do_bico, **kw):
        super().__init__(**kw)
        self.cor_do_bico = cor_do_bico


class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass
    

class Ornintorrinco(Mamifero, Ave):
    pass

animal_1 = Gato(nome = "Soda", num_patas = 4, cor_do_pelo = "Rajada Siamesa")
animal_2 = Ornintorrinco(nome = "Perry", num_patas = 4, cor_do_pelo ="Marrom",cor_do_bico = "Cinza")


print(animal_1)
print(animal_2)

