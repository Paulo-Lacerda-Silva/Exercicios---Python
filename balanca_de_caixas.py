"""
NOME: Controle de Recebimento de Caixas
O QUE FAZ:
Este programa ajuda a organizar a chegada das mercadorias.
Ele separa automaticamente as caixas leves das pesadas e já entrega o peso total
no final do turno, evitando erro de conta manual.
"""

leve = pesada = total = 0
peso = float(input('Digite o peso da caixa: '))
while peso != 0:
    total += peso
    if peso < 10:
        leve += 1
    if peso >= 10:
        pesada += 1
    peso = float(input('Digite o peso da caixa: '))
print('Voce tem {} caixas leves e {} caixas pesadas'.format(leve, pesada))
print('O peso total das caixas recebidas é de {}'.format(total))