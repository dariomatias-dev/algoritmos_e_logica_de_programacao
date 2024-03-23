import datetime

age = int(input("Digite a sua idade: "))

year = datetime.datetime.now().year

print("Ano de nascimento: {}".format(year-age))
