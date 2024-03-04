distanceToTravel = float(input("Digite a distância que deseja percorrer: "))
kilometersPerLiter = float(input("Digite a distância que o veículo faz por litro: "))

litersRequired = distanceToTravel/ kilometersPerLiter

print(
    "A quantidade de litros necessários será de: {} {}.".format(
        int(litersRequired) if int(litersRequired) == litersRequired else litersRequired,
        "litros" if litersRequired != 1 else "litro"
    ),
)
