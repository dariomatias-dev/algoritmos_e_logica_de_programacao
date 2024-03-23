name = input('Nome do funcionário: ')
workedHours = int(input('Quantidade de horas trabalhadas: '))
valuePerHour = int(input('Valor por hora: '))

print('O funcionário {} receberá: {}'.format(name, valuePerHour * workedHours))
