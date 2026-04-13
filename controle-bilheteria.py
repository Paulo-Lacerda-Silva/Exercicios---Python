"""
OBJETIVO: Monitorar o fluxo de vendas de ingressos em tempo real.
FUNCIONALIDADES:
- Registra valores de ingressos de forma dinâmica utilizando estrutura de repetição (while).
- Calcula o faturamento total acumulado e a quantidade de pessoas presentes.
- Possui gatilho de meta (R$ 100,00) para feedback instantâneo ao operador.
- Encerramento automático do caixa através de Flag (valor 0).
"""

ingresso = total = quant = 0
ingresso = float(input('Qual o valor do ingresso que você comprou: '))
while ingresso != 0:
    total += ingresso
    quant += 1
    if total >= 100:
        print('Meta batida!!! o estádio está enchendo')
    ingresso = float(input('Qual o valor do ingresso que você comprou: '))
print('O total arrecadado foi R${} e a quantidade de ingressos vendidos foi de {} ingressoas'.format(total, quant))