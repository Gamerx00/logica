# meu primeiro programa

from random import randint # importa a função de gerar numeros aleatórios

print("olá 1info2!")

dado1 = randint(1, 6) #gera um numero aleatorio entre 1 e 6

print("Dado1: ",dado1)

dado2 = randint(1, 6) #gera um numero aleatorio entre 1 e 6

print("Dado2: ",dado2)

dado3 = randint(1, 6) #gera um numero aleatorio entre 1 e 6

print("Dado3: ",dado3)

dado4 = randint(1, 6) #gera um numero aleatorio entre 1 e 6

print("Dado4: ",dado4)

jogador1 = dado1 + dado2
jogador2 = dado3 + dado4

print('jogador1', jogador1)
print('jogador2', jogador2)

if jogador1 > jogador2:
    print("jogador 1 venceu")
else:
    if jogador2 > jogador1:
     print("jogador 2 venceu")  