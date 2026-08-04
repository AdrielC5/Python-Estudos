# EXERCÍCIO 1 DE FUNÇÃO: QUADRADO DE UM NÚMERO

def exercicio1():

    numero = int(input("Digite um número: "))

    def quadrado(numero):
        resultado = numero * numero
        return resultado
    
    print(f"O quadrado de {numero} é: {quadrado(numero)}")

# #################################################################

# #EXERCÍCIO 2 DE FUNÇÃO: QUAL NÚMERO É MAIOR

def exercicio2():

    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))

    def maior_numero(numero1, numero2):
        if numero1 > numero2:
           return numero1
        else:
         return numero2
    
        print(f"O maior número é: {maior_numero(numero1, numero2)}")

# #################################################################

# #EXERCÍCIO 3 DE FUNÇÃO: APROVADO OU REPROVADO

def exercicio3():

    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))

    def media(nota1, nota2):
        resultado = (nota1 + nota2) / 2
        return resultado

        print(f"Sua média é de {media(nota1, nota2)}")

    if media(nota1, nota2)>= 7:
       print("Parabéns, você foi aprovado!")
    else:
      print("Infelizmente você está reprovado!") 

###############################################################

#EXERCÍCIO 4 DE FUNÇÃO: PAR OU ÍMPAR

def exercicio4():

    num1 = int(input("Digite um número: "))

    def par_ou_impar(num1):
        if num1 %2 == 0:
            return "Número Par"
        else:
            return "Número Impar"
    
    print(f"Seu número é um: {par_ou_impar(num1)}")

#########################################################

#EXERCÍCIO 5 DE FUNÇÃO: CALCULAR SE É MAIOR DE IDADE OU NÃO

def exercicio5():

    ano_nasc = int(input("Digite seu ano de nascimento: "))

    def calcular_idade(x):
        idade = int(2026 - ano_nasc)
        return idade

    print(f"Que legal! Então você tem: {calcular_idade(ano_nasc)} anos!")

    if calcular_idade(ano_nasc) >= 18:
        print("E você é maior de idade!")
    else:
        print("E você é menor de idade!")

############################################################

#EXERCÍCIO 6 DE FUNÇÃO: TABUADA

def exercicio6():

    numero_tabu = int(input("Digite um número para calcularmos na tabuada: "))

    def tabuada(x):
        for numero in range(1, 11):
            resultado = x * numero
            print(f"{x} x {numero} = {resultado}")

    tabuada(numero_tabu)

############################################################

#EXERCÍCIO 7 DE FUNÇÃO: SOMA DE LISTAS

def exercicio7():

    numeros = [10, 20, 30, 40]

    def somar_lista(numeros):
        soma = 0
        for numero in numeros:
            soma = soma + numero
            
        return soma
        
    print(f"A soma total da lista é de: {somar_lista(numeros)}")

###########################################################

#EXERCÍCIO 8 DE FUNÇÃO: PRINTAR O MAIOR NÚMERO DA LISTA

def exercicio8():

    numeros = [10, 25, 7, 40, 15, 200]

    def maior_lista(numeros):
        maior = numeros[0]
        for numero in numeros:
            if numero > maior:
                maior = numero
        return maior
    
    print(maior_lista(numeros))

###############################################################

#EXERCICIO 9 DE FUNÇÃO: MOSTRAR QUANTOS NUMEROS PARES TEM DENTRO DE UMA LISTA

def exercicio9():

    numeros = [ 10, 15, 69, 22, 67]

    def contar_pares(numeros):
        pares = 0
        for numero in numeros:
            if numero %2 == 0:
                pares = pares + 1
        return pares
       
    print(f"A quantidade de numeros pares dentro da lista é de: {contar_pares(numeros)}")

#######################################################################

#EXERCICIO 10 DE FUNÇÃÓ: RETORNA A MEDIA DE UMA LISTA

def exercicio10():

    numeros = [10, 20, 30, 40]
    
    def media_lista(numeros):
        
        soma = 0
        quantidade = len(numeros)

        for numero in numeros:
            soma = soma + numero
            media = soma / quantidade
        return media
        
    print(f"A média dessa lista é de: {media_lista(numeros)}")

########################################################################

#EXERCICIO 11 DE FUNÇÃO: MOSTRAR O MAIOR, MENOR E A MÉDIA DE UMA LISTA

def exercicio11():

    numeros = [10, 20, 30, 40, 50]

    def programa_pra_lista(numeros):

        soma = 0
        quantidade = len(numeros)
        maior = numeros[0]
        menor = numeros[0]

        for numero in numeros:
            soma = soma + numero
            
        media = soma / quantidade

        for numero in numeros:
            if numero > maior:
                maior = numero
                
        for numero in numeros:
            if numero < menor:
                menor = numero

        return media, maior, menor
        
    
    print(f"O programa foi executado! A Média, o Maior Número e o Menor Número são os respectivos: ")
    print(f"Resultado = {programa_pra_lista(numeros)}")

exercicio11()
        

        

            