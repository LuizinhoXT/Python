

class veiculo():
    
    def __init__(self, placa, num_rodas, peso, cor, marca, modelo):
       self.placa = placa
       self.num_rodas = num_rodas
       self.peso = peso
       self.cor = cor
       self.motor_ligado = False
       self.marca = marca
       self.modelo = modelo
       
       
       
    def ligar_motor(self):        
        self.motor_ligado = True
        
    def desligar_motor(self):
        self.motor_ligado = False
        
    def acelerar(self):
        print(f"{'acelerando' if self.motor_ligado else 'Não posso acelerar! o motor está desligado'}")
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
  
class motocicleta(veiculo):
    def __init__(self, placa, num_rodas, peso, cor, marca, modelo):
        super().__init__(placa, num_rodas, peso, cor, marca, modelo)
        
    def empinar(self):
        print("empinando!")
    
class carro(veiculo):
    def __init__(self, placa, num_rodas, peso, cor, marca, modelo, num_assentos,num_portas):
        super().__init__(placa, num_rodas, peso, cor, marca, modelo)
        self.num_assentos = num_assentos
        self.num_portas = num_portas
    
class caminhao(veiculo):
    def __init__(self, placa, num_rodas, peso, cor, marca, modelo, tamanho):
        super().__init__(placa, num_rodas, peso, cor, marca, modelo)
        self.carregado = False
        self.tamanho = tamanho
    def carregar_caminhao(self):
        self.carregado = True
    def descarregar_caminhão(self):
        self.carregado = False

carro2 = carro("abc-1234",4,1000,"preto","Mitsubishi","Lancer EVO X",5,4)
carro1 = carro("asd-3124",4,1400,"branco","Mazda","RX-8",4,2)
moto1 = motocicleta("lkj-7089",2,500,"cinza","Yamaha","CB-900")
caminhao1 = caminhao("lhk-0987",6,2000,"vermelho","Mercedes-Benz","Carroça 2018","médio")



print(caminhao1,"\n")
print(carro2,"\n")
print(carro1,"\n")
print(moto1,"\n")
