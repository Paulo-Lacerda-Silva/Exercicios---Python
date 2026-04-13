calorias = cont = soma = media = 0
calorias = int(input('Quantas calorias tem sua refeicao [Digite 0 para parar]: '))
while calorias != 0:
    cont += 1
    soma += calorias
    calorias = int(input('Quantas calorias tem sua refeicao [Digite 0 para parar]: '))
media = soma / cont
print('Voce teve {} refeições e o total de calorias foi de {}'.format(cont, soma))
print('A mérdia de calorias por refeição é de {:.2f}'.format(media))