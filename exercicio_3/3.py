value = int(input("Digite o número que quer ver a tabuada até 10: "))

for number in range(1, 11):
    print("{} x {} = {}".format(number, value, number * value))
