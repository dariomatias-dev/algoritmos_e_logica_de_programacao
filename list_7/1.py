numbers = []

for i in range(30):
    numbers.append(int(input("Insira o número da posição {}: ".format(i + 1))))


def greater(listOfNumbers):
    return max(listOfNumbers)


def smaller(listOfNumbers):
    return min(listOfNumbers)


def sum(listOfNumbers):
    result = 0

    for listOfNumber in listOfNumbers:
        result += listOfNumber

    return result


print("Maior:", greater(numbers))
print("Menor:", smaller(numbers))
print("Soma:", sum(numbers))
