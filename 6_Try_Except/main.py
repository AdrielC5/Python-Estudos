def exerciciotry():

    while True:
        try:
            numero1 = int(input("Digite um número: "))
            numero2 = int(input("Digite outro número: "))
            break
        except ValueError:
            print("Por favor, digite um número válido!")

    def maior_numero(numero1, numero2):
        if numero1 > numero2:
            return numero1
        else:
            return numero2

    print(f"O maior número é: {maior_numero(numero1, numero2)}")


####################################################################


def exerciciotry2():

    while True:
        try:
            nota1 = int(input("Digite a primeira nota: "))
            nota2 = int(input("Digite a segunda nota: "))
            break
        except ValueError:
            print("Por favor, digite um número válido! Tente novamente!")

    def media(nota1, nota2):
        resultado = (nota1 + nota2) / 2
        return resultado

    print(f"Sua média é de {media(nota1, nota2)}")

    if media(nota1, nota2) >= 7:
        print("Parabéns, você foi aprovado!")
    else:
        print("Infelizmente você está reprovado!")


#####################################################################


def exerciciotry3():

    while True:
        try:
            num1 = int(input("Digite um número: "))
            break
        except ValueError:
            print("Por favor, digite um número válido! Tente Novamente")

    def par_ou_impar(num1):
        if num1 % 2 == 0:
            return "Número Par"
        else:
            return "Número Impar"

    print(f"Seu número é um: {par_ou_impar(num1)}")


#######################################################################


def exerciciotry4():

    while True:
        try:
            ano_nasc = int(input("Digite seu ano de nascimento: "))
            break
        except ValueError:
            print("Por favor, digite um número válido! Tente Novamente!")

    def calcular_idade(x):
        idade = int(2026 - ano_nasc)
        return idade

    print(f"Que legal! Então você tem: {calcular_idade(ano_nasc)} anos!")

    if calcular_idade(ano_nasc) >= 18:
        print("E você é maior de idade!")
    else:
        print("E você é menor de idade!")

exerciciotry2()
