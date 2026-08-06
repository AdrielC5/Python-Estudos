def exercicioarq1():
    nome = input("Olá, digite seu nome por favor: ")

    with open("usuarios.txt", "a") as arquivo:
       arquivo.write(nome + "\n")

    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            print(linha)

def exercicioarq2():
    import csv

    nome = input("Olá, digite seu nome por favor: ")

    while True:
        try:
            idade = int(input("Agora, digite sua idade: "))
            break
        except ValueError:
            print("Digite um número válido!")

    cidade = input("Agora, digite a cidade onde mora: ")

    with open("pessoas.csv", "a", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, idade, cidade])

    with open("pessoas.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)

exercicioarq2()