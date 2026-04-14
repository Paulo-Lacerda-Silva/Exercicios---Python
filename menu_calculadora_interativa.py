"""
NOME: Menu Interativo de Operações Matemáticas
O QUE FAZ:
Este programa funciona como uma central de cálculos. Ele permite que o usuário
escolha entre somar, multiplicar ou descobrir qual número é maior.
Também permite trocar os números sem precisar fechar o programa e tem uma
saída elegante com delay (sleep).
"""


from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
print('-' * 30)
while opcao != 5:
    print('''    [1] - SOMAR
    [2] - MULTIPLICAR
    [3] - MAIOR
    [4] - NOVOS NÚMEROS
    [5] - SAIR DO PROGRAMA''')
    opcao = int(input('Escolha uma opcao '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('O resultado da multiplicação entre {} e {} é de {}'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1.5)
print('Fim do programa')