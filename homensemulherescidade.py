listahomens = []
listamulheres = []

while True:
    sexo = int(input('Qual o sexo da pessoa?\n'
                     '1 - Masculino\n'
                     '2 - Feminino\n'
                     '* Se não tem mais pessoas\n'
                     'e você quer encerrar o programa para saber a quantidade\n'
                     'de homens e mulheres na cidade digite "0". *\n'
                     ': '))
    if sexo == 0:
        break
    elif sexo == 1:
        listahomens.append(sexo)
    else:
        listamulheres.append(sexo)

print(f'\nTotal de pessoas na cidade: {len(listahomens) + len(listamulheres)}\n')

print(f'Existem {len(listahomens)} homens na cidade. Ou seja,\n'
      f'{((len(listahomens) * 100) / (len(listahomens) + len(listamulheres))):.2f}'
      f'% do total de pessoas.\n')

print(f'Existem {len(listamulheres)} mulheres na cidade. Ou seja,\n'
      f'{((len(listamulheres) * 100) / (len(listahomens) + len(listamulheres))):.2f}'
      f'% do total de pessoas.')

