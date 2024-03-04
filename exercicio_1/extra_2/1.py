dollarQuote = float(input("Digite a cotação do dolar: "))
dollarsForConversation = float(input("Digite o valor que quer converter: "))

amountOfReais = dollarsForConversation * dollarQuote

print("Quantidade de reais: R$ {:.2f}".format(amountOfReais))
