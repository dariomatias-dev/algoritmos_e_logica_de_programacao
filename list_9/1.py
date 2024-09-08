import os

parts = []


def addPart():
    return parts.pop()


def removePart(name):
    parts.append(name)


def clear():
    os.system("cls")


stop = False

while not stop:
    action = input("Remover (r) ou Montar (m)? ")

    if action == "r":
        name = input("Digite o nome da peça que removeu: ")

        removePart(name)
        clear()
    elif action == "m":
        stop = True

        print("")
        clear()

        for _ in range(len(parts)):
            print(addPart())
    else:
        clear()
        print("Operação inválida.")
