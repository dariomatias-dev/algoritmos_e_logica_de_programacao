matrix = []
for line in range(2):
    values = []

    for col in range(2):
        values.append(
            int(input("Insirá o valor da linha {} coluna {}: ".format(line, col))),
        )

    matrix.append(values)

result = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

print("Determinante:", result)
