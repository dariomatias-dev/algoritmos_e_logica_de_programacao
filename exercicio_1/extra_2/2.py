nameOfTheStudent = input("Nome do aluno: ")
testScore1 = float(input("Nota da primeira prova: "))
testScore2 = float(input("Nota da segunda prova: "))
testScore3 = float(input("Nota da terceira prova: "))
testScore4 = float(input("Nota da quarta prova: "))

average = (testScore1 + testScore2 + testScore3 + testScore4)/ 4

print("---------------------------------------------")
print("Nome do aluno:", nameOfTheStudent)
print("Média de {} é: {:.1f}".format(nameOfTheStudent, average))
