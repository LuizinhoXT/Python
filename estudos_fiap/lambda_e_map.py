# aplicaç~ao, função lambda e MAP

triplo = lambda num : num * 3
isBool = lambda val : "verdadeiro" if val == 1 else "negativo"

def soma (a,b):
    soma = a + b
    return soma


dados = [2,4,6,8,10]
bools = [0,0,1,0,0,1,0,1,1,1]

saida_1 = list(map(triplo, dados))
saida_2 = list(map(bool, bools))
saida_3 = soma(2, b = 4)

def calculaForca(peso,aceleracao):
   forca = aceleracao * peso

   print(f"forca necessária é: {forca}")

p = float(input("digite peso: "))
a = float(input("digite aceleracao: "))


calculaForca(p,a)




