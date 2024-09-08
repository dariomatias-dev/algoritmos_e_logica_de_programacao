import os


regulars = []


def addRegular(name):
    regulars.append(name)
    print("Paciente regular adicionado com sucesso.")


def removeRegular(name):
    if name in regulars:
        regulars.remove(name)
        print("Paciente regular removido com sucesso.")
    else:
        print("Paciente regular não existe na lista.")


priorities = []


def addPriority(name):
    priorities.append(name)
    print("Paciente prioritário adicionado com sucesso.")


def removePriority(name):
    if name in priorities:
        priorities.remove(name)
        print("Paciente prioritário removido com sucesso.")
    else:
        print("Paciente prioritário não existe na lista.")


def getListType():
    listType = ""

    validListType = False
    while not validListType:
        listType = input("Lista regular (r) ou prioridade (p)? ")

        if listType not in ["r", "p"]:
            clear()
            print("Ação inválida.")
        else:
            validListType = True

    return listType


def clear():
    os.system("cls")


clear()

stop = False

while not stop:
    action = input(
        "Adicionar (add) paciente, remover (rem) paciente, atender paciente (att) ou encerrar programa (stop)? ",
    )

    clear()

    if action == "stop":
        print("Programa encerrado.")
        stop = True
    elif action == "add":
        listType = getListType()

        clear()

        name = input("Qual o nome do paciente a ser adicionado a lista? ")

        clear()

        if listType == "r":
            addRegular(name)
        else:
            addPriority(name)
    elif action == "rem":
        listType = getListType()

        clear()

        patientList = []
        if listType == "r":
            patientList = regulars
        else:
            patientList = priorities

        if len(patientList) == 0:
            clear()
            print("Ainda não há pacientes para remover.")
        else:
            name = input("Qual o nome do paciente a ser removido da lista? ")

            if listType == "r":
                removeRegular(name)
            else:
                removePriority(name)
    elif action == "att":
        clear()

        isPriority = True
        for _ in range(len(regulars) + len(priorities)):
            clear()
            if isPriority and len(priorities) != 0:
                print("Paciente para atendimento:", priorities[0])
                priorities.pop(0)
                isPriority = False
            else:
                print("Paciente para atendimento:", regulars[0])
                regulars.pop(0)
                isPriority = True

            if len(regulars) + len(priorities) == 0:
                print("Não há mais pacientes para atendimento.")
                break

            confirm = input("Próximo (prox) ou parar (stop)? ")

            if confirm == "stop":
                break

    else:
        print("Ação inválida.")
