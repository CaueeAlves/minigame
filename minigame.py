import random
import os
erros = 0
n_sorteado = random.randrange(0,10)
n_jogador = int(input('digite seu numero'))

if(n_sorteado > n_jogador) or (n_sorteado < n_jogador):
    print('erro, digite outro numero')
    erros+=1
    n_jogador = int(input('digite seu numero'))
    n_jogador = int(input('digite outro numero'))
    n_jogador = int(input('ultima chance '))
    n_jogador = int(input('Voce atingiu o limite maximo de tentativas'))

elif(n_sorteado == n_jogador):
    print('voce acertou em ' + str(erros+1) + ' tentativas ')








