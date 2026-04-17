"""
PROJETO: Gerador de Tabuada Interativo
OBJETIVO: Calcular a tabuada de qualquer número inteiro conforme a solicitação do usuário.
DIFERENCIAL:
- Utiliza um laço 'while' para permitir múltiplas consultas na mesma execução.
- Implementa um laço 'for' aninhado para processamento da lógica matemática.
- Tratamento de string para facilitar a navegação do utilizador (S/N).
"""
resp = 'N'
num = int(input('Digite um número para saber sua tabuada: '))
for c in range(1, 11):
    print('{} X {} = {}'.format(num, c, num * c))
resp = str(input('Quer continuar [S/N] ? ')).strip().upper()[0]
if resp in 'S':
    while resp == 'S':
        num = int(input('Digite um número para saber sua tabuada: '))
        for c in range(1, 11):
            print('{} X {} = {}'.format(num, c, num * c))
        resp = str(input('Quer continuar [S/N] ? ')).strip().upper()[0]
print('Fim do programa')