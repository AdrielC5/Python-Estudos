def exercicioarq1():
    nome = input("Olá, digite seu nome por favor: ")

    with open("usuarios.txt", "a") as arquivo:
       arquivo.write(nome + "\n")

    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            print(linha)

exercicioarq1()