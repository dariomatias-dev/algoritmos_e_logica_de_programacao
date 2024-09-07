dimensions = int(input("Insirá a dimensão da matriz: "))

result = 0
for line in range(dimensions):
    for col in range(dimensions):
        result += int(
            input(
                "Digite o valor da linha {} coluna {}: ".format(line, col),
            )
        )

print("Resultado do produto escalar:", result)
