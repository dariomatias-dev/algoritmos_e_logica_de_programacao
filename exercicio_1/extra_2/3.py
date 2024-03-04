C = float(input("Digite a temperatura em Celsius: "))

F = (9 * C + 160)/ 5

print("Temperatura em Fahrenheit: {} graus Fahrenheit".format(int(F)  if F == int(F) else F))
