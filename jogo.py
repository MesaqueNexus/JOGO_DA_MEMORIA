# JOGO DA MEMÓRIA
# By Mesaque
# Python 3.9.0
from random import randint
from time import sleep
from os import supports_follow_symlinks, system

numeros = []
respostas = []

def header():
    print('''
#==========================#
#====  JOGO DA MEMÓRIA  ===#
#==========================#
    ''')

def gerador_de_números():
    i = 0
    while i < 4:
        numero = randint(0, 100)
        numeros.append(numero)
        i += 1

def inicializar():
    print('Carregando jogo...')
    sleep(2)
    print('Vamos começar!')
    for n in range(0, 3):
        print(n)
        sleep(0.6)
    print('Gooooo!!')
    sleep(1)
    system('cls')
    header()


while True:
    gerador_de_números()
    header()
    inicializar()
    tentativas = 3
    i = 1
    while i <= 4:
        for n in numeros:
            print(f'[   {n}   ]', end='', flush=True)
            sleep(1.5)
            i += 1
    while tentativas > 0:
        system('cls')
        print(f'Você tem {tentativas} tentativas.')
        cont = 1
        while cont < 5:
            print(f'QUAL O {cont}º NÚMERO DA SEQUÊNCIA?')
            resposta = int(input('>>> '))
            respostas.append(resposta)
            cont += 1
        if numeros == respostas:
            print(f'Parabéns você venceu com {tentativas} tentativas restantes...')
            break
        else:
            print('Sequência incorreta :(')
            respostas.clear()
            tentativas -= 1
            cont = 1
            continue
    if numeros != respostas:
        print('VOCÊ PERDEU :(')
    x = input('deseja jogar novamente?[S/N] ').upper()
    if x == 'S' or x == 'SIM':
        numeros.clear()
        respostas.clear()
        continue
    else:
        print('Obrigado por jogar\nAté logo!')
        break