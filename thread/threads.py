from threading import Thread
import time

def carro(velocidade, modelo):
    trajeto_km = 0
    while trajeto_km <= 100:
        print(f"modelo : {modelo}, conclusão : {trajeto_km}")
        trajeto_km+=velocidade
        time.sleep(0.2)





__carro1 = Thread(target=carro, args= [2, "Civic Typer R"])
__carro2 = Thread(target=carro, args= [5, "BMW M3 GTR"])

__carro1.start()
__carro2.start()
