import random
from time import sleep
def escolheu():
    n = bot
    if n == 1:
        print("O bot escolheu Pedra!!")
    elif n == 2:
        print("O bot escolheu Papel!!")
    else:
        print("O bot escolheu Tesoura!!")

def pedra():
    global v
    global e
    global p
    if bot == 1:
        print("Empatou!!")
        e += 1
    elif bot == 2:
        print("Você perdeu!")
        p += 1
    elif bot == 3:
        print("Você ganhou!!")
        v += 1

def papel():
    global v
    global e
    global p
    if bot == 1:
        print("Você ganhou!!")
        v += 1
    elif bot == 2:
        print("Empatou!")
        e += 1
    elif bot == 3:
        print("Você perdeu!!")
        p += 1

def tesoura():
    global v
    global e
    global p
    if bot == 1:
        print("Você perdeu!!")
        p += 1
    elif bot == 2:
        print("Você ganou!")
        v += 1
    elif bot == 3:
        print("Empatou!")
        e += 1

def contagem():
    for c in range(0, 3):
        print(".", end="")
        sleep(1.0)
    print("\nPedra")
    sleep(1.3)
    print("Papel")
    sleep(1.3)
    print("Tesooooouuuuraaa!!")
    sleep(1.1)


print("Pedra, papel ou tesoura!! Vamos jogar??")
n = 1
v = 0
e = 0
p = 0
while True:
    try:
        n = int(input("Digite [1] para jogar ou digite [0] para finalizar: "))
        if n == 1:
            print("Beleza vamos jogar!!")
            n = int(input("Digite [1] caso queira 'Pedra', [2] caso queira 'Papel' ou [3] caso queira 'Tesoura': "))
            if n == 1:
                print("Vamos de pedra então!!")
                contagem()
                bot = random.randint(1, 3)
                escolheu()
                pedra()
            elif n == 2:
                print("Vamos de papel então!!")
                contagem()
                bot = random.randint(1, 3)
                escolheu()
                papel()
            elif n == 3:
                print("Vamos de tesoura então!!")
                contagem()
                bot = random.randint(1, 3)
                escolheu()
                tesoura()
            else:
                print("Valor invalido!")
        elif n == 0:
            break
        else:
            print("Valor invalido!!")
    except:
        print("Valor invalido!!")
finaly:
    print(f"Você ganhou {v} vezes, perdeu {p} vezes e empatou {e} vezes!")
