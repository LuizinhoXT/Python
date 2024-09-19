class Passaro():
    def __init__(self):
        pass
    def voar(self):
        print(f"a(o) {__class__.__name__} está voando")

class Arara(Passaro):
    pass

class Galinha(Passaro):
    def voar(self):
        print(f"o animal morreu pq {__class__.__name__} não pode voa")
        
class Pinguim(Passaro):
    def voar(self):
        print(f"o animal morreu pq {__class__.__name__} não pode voa")

class Aeronave():
    def __init__(self):
        pass
    def receber_passageiro(self):
        print("passageiros entrando...")
        
class Pombo(Passaro):
    pass

class Calopsita(Passaro):
    pass

class Galo(Passaro):
    def voar(self):
        print(f"o animal morreu pq {__class__.__name__} não pode voa")

    
class Aviao(Passaro, Aeronave):
    pass
def jogar_pela_janela_do_ap(obj):
    obj.voar()
    
GIsele = Galinha()
Blue = Arara()
Caduh = Pinguim()
Joao_Frango = Galo()
Nijahel = Calopsita()
marcos = Pombo()

Aviaozinho = Aviao()

jogar_pela_janela_do_ap(GIsele)
jogar_pela_janela_do_ap(Blue)
jogar_pela_janela_do_ap(Caduh)
jogar_pela_janela_do_ap(Joao_Frango)
jogar_pela_janela_do_ap(Nijahel)
jogar_pela_janela_do_ap(marcos)


Aviaozinho.voar()
Aviaozinho.receber_passageiro()