class Lutador:
    def __init__(self,nome, nacionalidade, altura, idade, peso, vitorias, derrotas, empates):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.altura = altura
        self.idade = idade
        self.peso = peso
        self.categoria = self.set_categoria()
        self.vitorias = vitorias
        self.derrotas = derrotas
        self.empates = empates

    def set_categoria(self):
        if self.peso <= 52.2:
            return "Inválido"
        elif self.peso <= 70.3:
            return "Leve"
        elif self.peso <= 83.9:
            return "Médio"
        elif self.peso <= 120.2:
            return "Pesado"
        else:
            return "Inválido"    
    def apresentar(self):
        msg = f"""
        \n
        Lutador: {self.nome} \n 
        Origem: {self.nacionalidade} \n
        Ele têm {self.idade} Anos \n
        Ele têm {self.altura} de altura \n
        Pesando {self.peso} kg \n
        Possui {self.vitorias} vitórias \n
        perdeu {self.derrotas} vezes \n
        e empadou {self.empates} vezes \n
        
        
        """
        print(msg)
        
        pass
    def status(self):
        msg = f"{self.nome} é um peso {self.categoria} com {self.vitorias}, {self.derrotas} derrotas e {self.empates} empates."
        
        print(msg)
        pass
    def ganhar_luta(self):
        self.vitorias = self.vitorias + 1
    def perder_luta(self):
        self.derrotas = self.derrotas + 1
    def empatar_luta(self):
        self.empates = self.empates + 1