numbers = []
value = 2

while len(numbers) != 100:
    add = True

    for i in range(2, value):
        if value % i == 0:
            add = False
            break

    if add:
        print(value)
        numbers.append(value)

    value += 1


def sum(listOfNumbers):
    result = 0
    for listOfNumber in listOfNumbers:
        result += listOfNumber

    return result


print("Soma:", sum(numbers))
