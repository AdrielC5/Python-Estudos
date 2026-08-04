nome = input("Qual o seu nome?: ")

print(f"Prazer {nome}! Vi que você está querendo tirar a sua carteira de habilitação.")

idade = int(input(f"{nome}, Qual a sua idade?: "))

if idade >= 18: 
    print(f"Entendi {nome}! Então você é maior de idade! Pode começar a tirar! ")
else:
    print(f"Putz {nome}, Você é menor de idade! Ainda não pode tirar! ")



