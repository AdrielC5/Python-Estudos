numeros = [ 10, 15, 69, 22, 67]

def contar_pares(numeros):
    return len([numero for numero in numeros if numero % 2 == 0])

print(contar_pares(numeros))

# A FORMA ACIMA É UM EXEMPLO DO TERMO "LIST COMPREHENSION" QUE NO CASO ELE PEGA E ENCURTA UMA LINHA EXTENSA
# DE UM CÓDIGO E ENCURTA EM APENAS UMA LINHA SÓ.

def somar_pares(numeros):

    soma = sum([numero for numero in numeros if numero % 2 == 0])
    return soma  # 32

print(somar_pares(numeros))

# JÁ NESSE EXEMPLO ACIMA EU FIZ O LIST COMPREHENSION NOVAMENTE, ENCURTANDO A LINHA DO CÓDIGO. EM VEZ DE
# CRIAR UMA VARIÁVEL SOMA = 0, EU JÁ FIZ A SOMA COM O COMANDO SUM(), EM UMA ÚNICA LINHA DO CÓDIGO, E SOMEI
# APENAS OS NÚMEROS PARES.