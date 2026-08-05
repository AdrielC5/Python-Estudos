def exerciciosplit():
    frase = input("Digite uma frase qualquer: ")
    palavras = frase.split()

    print(f"A frase tem {len(palavras)} palavras")
    print(f"A última palavra é: {palavras[-1]}")

##################################################

def exerciciojoin():
    frase = input("Digite uma frase aleatória: ")
    palavras = frase.split()
    frase_nova = "-".join(palavras)

    print(f"{frase_nova}")

##################################################

def exercicio_upper_lower_strip():
    email = input("Digite seu e-mail: ").lower().strip()
    print (f"Bem vindo, seu email é: {email}")

exercicio_upper_lower_strip()