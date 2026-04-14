"""
NOME: Jogo da Adivinhação (Humano vs Computador)
O QUE FAZ:
O computador sorteia um número secreto e desafia o usuário a acertar.
O programa dá dicas se o número correto é maior ou menor que o palpite atual
e, no final, revela quantas tentativas foram necessárias para vencer.
TECNOLOGIAS: Biblioteca Random, Loop While com Booleano e Contadores.
"""

from random import randint
computador = randint (0, 10)
acertou = False
palpites = 0
print('Estou pensando em um número entre 0 e 10.')
while not acertou:
    palpites += 1
    jogador = int(input('Tente adivinhar qual é: '))
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez: ')
        elif jogador > computador:
            print('Menos... Tente mais uma vez: ')

print('Voce acertou com {} palpites'.format(palpites))

