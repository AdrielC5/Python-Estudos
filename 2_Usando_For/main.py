nomes = [] #CRIA UMA LISTA VAZIA, NO CASO "NOMES" É O NOME DA LISTA

#Aqui eu peço um nome para ser armazenado dentro da variável "nomenovo" com o comando INPUT
nomenovo = input("Digite seu nome: ") 

#Aqui eu crio uma FUNÇÃO que recebe um nome e logo após abaixo fiz essa função exibir uma mensagem sempre que chamada
def boas_vindas(nome):
    print(f"Bem vindo ao meu programa {nome}")

#Aqui estou chamando a função, porém dentro do paranteses coloquei a variável "nomenovo", permitindo assim sempre
#que chamada, a mensagem de saudação será com o nome que a variável recebe lá no inicio com o INPUT.
boas_vindas(nomenovo)

#Aqui já é o uso do FOR, que no caso significa "PARA"
#Por exemplo, nesse for, ele está com a função de repetir 3 vezes o comando dentro dele, que no caso é o while
#pedindo que o usuário digite um nome.
for x in range(3):
    while True:             #aqui nesse caso o while só vai ser TRUE se o usuário digitar um nome válido
        nome = input("DIGITE UM NOME: ")
        if nome.isalpha():  #e só será um nome valido, se não tiver numeros, apenas letras, por conta desse comando aqui
            nomes.append(nome)
            break
        else:       #se não for um nome válido, ele vem para o else e aparece a mensagem e executa o código novamente
            print("DIGITE UM NOME VÁLIDO: ") #até o usuário digitar um nome válido.

for nome in nomes:
    print(nome)

#esse ultimo FOR aqui em cima, está falando "PARA nome em NOMES < que no caso é a lista vazia = print(nome)"
#no caso está pedindo para printar, ou seja, mostrar ao usuário cada nome que está dentro da lista vazia, que já não
#está mais vazia, por conta que assim que adicionamos um nome "Válido" o comando "nomes.append(nome)" adicionou
#os nomes dentro da nossa lista vazia.


