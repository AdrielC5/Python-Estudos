def exerciciosplit():
    frase = input("Digite uma frase qualquer: ")
    palavras = frase.split() #split faz a frase digitada ser separada em palavras únicas

    print(f"A frase tem {len(palavras)} palavras")
    print(f"A última palavra é: {palavras[-1]}")

##################################################

def exerciciojoin():
    frase = input("Digite uma frase aleatória: ")
    palavras = frase.split()
    frase_nova = "-".join(palavras) #join une palavras em uma unica frase

    print(f"{frase_nova}")

##################################################

def exercicio_upper_lower_strip():
    email = input("Digite seu e-mail: ").lower().strip() #lower = minuscula | strip = deleta espaços em branco
    print (f"Bem vindo, seu email é: {email}")