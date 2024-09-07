# Exemplo para testes:
# matrix1 = [
#     [2, 0, 1],
#     [5, 3, 2],
# ]
#
# matrix2 = [
#     [4, 3],
#     [1, 2],
#     [0, 6],
# ]

matrixRows1 = int(input("Quantidade de linhas da matriz 1: "))
matrixColumns1 = int(input("Quantidade de colunas da matriz 1: "))

matrixRows2 = int(input("Quantidade de linhas da matriz 2: "))
matrixColumns2 = int(input("Quantidade de colunas da matriz 2: "))


def createMatrix(number, matrixRows, matrixColumns):
    matrix = []
    for line in range(matrixRows):
        values = []

        for col in range(matrixColumns):
            values.append(
                int(
                    input(
                        "Insirá o valor da linha {} coluna {} da matriz {}: ".format(
                            line, col, number
                        )
                    )
                ),
            )

        matrix.append(values)

    return matrix


if matrixColumns1 != matrixRows2:
    print("Não é possível calcular a multiplicação das matrizes.")
else:
    matrix1 = createMatrix(1, matrixRows1, matrixColumns1)
    matrix2 = createMatrix(2, matrixRows2, matrixColumns2)

    result = []

    for line in range(len(matrix1)):
        values = []

        for loop in range(len(matrix1)):
            value = 0
            for col in range(len(matrix1[0])):
                value += matrix1[line][col] * matrix2[col][loop]
            values.append(value)

        result.append(values)

    print("Resultado da multiplicação das duas matrizes", result)
