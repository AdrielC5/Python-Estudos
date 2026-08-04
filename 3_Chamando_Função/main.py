while True:             
        nome = input("DIGITE SEU NOME: ")
        if nome.isalpha():
            break
        else:       
            print("DIGITE UM NOME VÁLIDO: ")

def saudacao(nome):
    if nome == "Adriel" :
          print(f"Olá, {nome}! Que bom te ver novamente! ")
    else:
         print(f"Olá, {nome}! Seja bem-vindo(a)!")

saudacao(nome)

#Aqui neste exercício, as primeiras linhas copiei apenas o código do exercício 2, que faz com que o código peça um
#nome ao usuário, e se o nome tiver caracteres especiais ou números, ele mostra a mensagem de nome inválido, pois
#usei o comando nome juntamente do comando ".isalpha" que faz com que não permita caracteres especiais e nem números

#Agora da linha 8 em diante, aprendi a criar uma FUNÇÃO e chama-lá, e dentro da função coloquei o comando IF e ELSE
#que caso o nome que eu colocasse lá no inicio fosse igual (==) a "Adriel", ele me mostra uma mensagem personalizada
#Agora se eu coloco qualquer outro nome lá em cima no primeiro momento que ele me pede, o ELSE me mostra outra coisa
#No caso, outra mensagem, uma mensagem de boas vindas, como se fosse um usuário novo acessando pela primeira vez.