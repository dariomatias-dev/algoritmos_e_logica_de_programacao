fileSize = int(input("Informe o tamanho de um arquivo para download (em MB): "))
linkSpeed = int(input("Informe a velocidade de um link de Internet (em MBps): "))

time = int(fileSize/ linkSpeed)

minutes = int(time/60) if time >= 60 else 0
seconds = time % 60

print(
    "{} {} e {} {}.".format(
        minutes,
        "minuto" if minutes == 1 else "minutos",
        seconds,
        "segundo" if seconds == 1 else "segundos",
    )
)
