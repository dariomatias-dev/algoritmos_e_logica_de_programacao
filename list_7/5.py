names = []

for i in range(10):
    names.append(input("Insirá o nome {}: ".format(i + 1)))

names.sort()

for i in range(10):
    print(names[i])
