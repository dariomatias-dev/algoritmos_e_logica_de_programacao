lowerBound = int(input("Digite o limite inferior: "))
upperBound = int(input("Digite o limite superior: "))

numbers = []

for v in range(lowerBound, upperBound + 1):
    result = v**2
    numbers.append(result)
    print(result)


def sum(listOfNumbers):
    result = 0
    for listOfNumber in listOfNumbers:
        result += listOfNumber

    return result


print("Soma:", sum(numbers))
