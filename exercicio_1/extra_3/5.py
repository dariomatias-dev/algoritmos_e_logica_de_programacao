listNote = float(input("Informe a nota das listas: "))
projectNote = float(input("Informe a nota do projeto: "))
testNote = float(input("Informe a nota das provas: "))

result = (listNote * 20 + projectNote * 30 + testNote * 50)/ 100

print("A média é: ", result)
