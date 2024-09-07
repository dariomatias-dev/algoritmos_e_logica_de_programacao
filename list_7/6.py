numbers = []

for i in range(10):
    numbers.append(int(input("Insirá o número {}: ".format(i + 1))))

numbers.sort()

for i in range(9, 0, -1):
    print(numbers[i])
