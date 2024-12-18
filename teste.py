import time
import random
casa = ["Katana",(['Dano',10], ["Velocidade",6], ["Peso",7.5])]
for x in range(6):
    d6 = random.randint(0,6)
    time.sleep(0.2)
    print(f"\r{d6}",end="")
