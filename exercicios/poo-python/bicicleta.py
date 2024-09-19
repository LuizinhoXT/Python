class Bicicleta:
    def __init__(self,cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor 
        
    def buzinar(self):
        print("Prim Plim")
        
    def correr(self):
        print("Bicicleta corendo")
        
    def parar(self):
        print("bicicleta parada")
    def __str__(self):
        return f"{__class__}: {[f'{chave}= {valor}' for chave,valor in self.__dict__.items()]}"
        
b1 = Bicicleta("vermelha", "BMX", "2023", 3000)


b2 = Bicicleta("preta", "monark", "2022", 2000)

print(b2.__str__())
print(b1.__str__())
