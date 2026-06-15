times = {
    "Brasil": {"pontos": 0},
    "Argentina": {"pontos": 0},
    "França": {"pontos": 0},
    "Espanha": {"pontos": 0}
}

while True:
    print("\n=== COPA DO MUNDO 2026 ===")
    print("1 - Registrar jogo")
    print("2 - Ver classificação")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        time1 = input("Time 1: ")
        gols1 = int(input("Gols do Time 1: "))
1
        time2 = input("Time 2: ")
        gols2 = int(input("Gols do Time 2: "))

        if gols1 > gols2:
            times[time1]["pontos"] += 3
        elif gols2 > gols1:
            times[time2]["pontos"] += 3
        else:
            times[time1]["pontos"] += 1
            times[time2]["pontos"] += 1

        print("Resultado registrado!")

    elif opcao == "2":
        print("\n=== CLASSIFICAÇÃO ===")

        ranking = sorted(
            times.items(),
            key=lambda x: x[1]["pontos"],
            reverse=True
        )

        for pos, (time, dados) in enumerate(ranking, start=1):
            print(f"{pos}º {time} - {dados['pontos']} pontos")

    elif opcao == "3":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")
        