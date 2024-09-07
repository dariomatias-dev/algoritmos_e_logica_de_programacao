averages = 0

for i in range(40):
    grade1 = input("Nota 1 Bimestre:")
    grade2 = input("Nota 2 Bimestre:")
    grade3 = input("Nota 3 Bimestre:")
    grade4 = input("Nota 4 Bimestre:")

    average = (grade1 + grade2 + grade3 + grade4) / 4

    averages += average

print(averages / 40)
