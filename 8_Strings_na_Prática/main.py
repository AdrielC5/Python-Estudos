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

##################################################

def exerciciofatiamento():
    palavra = input("Digite uma palavra: ")
    print(palavra[:3]) #puxa as três PRIMEIRAS letras da palavra que o usuário digitou
    print(palavra[3:]) #pega da terceira POSIÇÃO da palavra que o usuário digitou em diante
    print(palavra[-3:]) #puxa as três ÚLTIMAS letras da palavra que o usuário digitou por conta do -
    print(palavra[: :-1]) #faz a palavra digitada pelo usuário se INVERTER, ficando de trás pra frente

# LEMBRANDO QUE A CONTAGEM COMEÇA EM 0 E NÃO EM 1 !!!!!!

exerciciofatiamento()