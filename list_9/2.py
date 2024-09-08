import os

patients = []


def addPatient(patient):
    patients.append(patient)
    print("Vez do paciente:", len(patients))


def removePatient(patient):
    if patient in patients:
        patients.remove(patient)
        print("Paciente removido com sucesso.")
    else:
        print("Nome do paciente não existe na lista.")


def clear():
    os.system("cls")


clear()

stop = False

while not stop:
    action = input(
        "Adicionar (add) paciente, remover (rem) paciente ou encerrar programa (stop)? ",
    )

    clear()

    if action == "add":
        name = input("Qual o nome do paciente a ser adicionado a lista? ")
        addPatient(name)
    elif action == "rem":
        if len(patients) == 0:
            print("Ainda não há pacientes para remover.")
        else:
            name = input("Qual o nome do paciente a ser removido da lista? ")
            removePatient(name)
    elif action == "stop":
        print("Programa encerrado.")
        stop = True
    else:
        print("Ação inválida.")
