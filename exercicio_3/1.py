value = int(input('Digite o valor inteiro de reais: '))

notesOf50 = 0
notesOf10 = 0
notesOf5 = 0
notesOf1 = 0

notesOf50 = value // 50
value %= 50

notesOf10 = value // 10
value %= 10

notesOf5 = value // 5
value %= 5

notesOf1 = value // 1
value %= 1


print("Notas de 50: {}".format(notesOf50))
print("Notas de 10: {}".format(notesOf10))
print("Notas de 5: {}".format(notesOf5))
print("Notas de 1: {}".format(notesOf1))
