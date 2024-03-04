salary = float(input("Digite o salário do funcionário: "))

bonus = salary * 0.6

print("Bonûs de natal é de: R$ {:.2f}".format(bonus))
print("Valor a ser depositado na conta de cada empregado: R$ {:.2f}".format(salary + bonus))
