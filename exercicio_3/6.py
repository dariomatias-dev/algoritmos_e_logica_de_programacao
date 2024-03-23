name = input('Nome do vendedor: ')
fixedSalary = float(input('Salário fixo: '))
salesAmount = float(input('Total de vendas: '))

commission = salesAmount * 0.15

print('Salário total que o vendedor(a) {} recebeu: R$ {}'.format(name, fixedSalary + commission))
print('Comissão que {} recebeu: R$ {}'.format(name, commission))
