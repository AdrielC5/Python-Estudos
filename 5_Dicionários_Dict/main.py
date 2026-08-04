#EXERCÍCIO 1 - CRIANDO MEU PRIMEIRO DICIONÁRIO:

def dicionario1():

    produto = {
        
        "nome": "Notebook",
        "valor": 2500,
        "quantidade": 10
    }
    print(produto["nome"])
    print(produto["valor"])
    print(produto["quantidade"])

    print(produto["valor"] * produto["quantidade"])

#####################################################

#EXERCÍCIO 2 DE DICIONÁRIO - APROVADO OU REPROVADO:

def dicionario2():

    aluno = {
        "nome": "Adriel",
        "nota1": 7,
        "nota2": 10
    }

    media = ((aluno["nota1"] + aluno["nota2"]) /2)

    print(media)

    if media >= 7:
        print(f"{aluno['nome']} foi aprovado!")
    else:
        print(f"{aluno['nome']} foi reprovado.")

####################################################

#EXERCÍCIO 3 - VERIFICAR ALUNO:

def dicionario3():

    def verificar_aluno(aluno):

        media = ((aluno["nota1"] + aluno["nota2"]) /2)

        if media >= 7:
            return(f"{aluno['nome']} foi aprovado!")
        else:
            return(f"{aluno['nome']} foi reprovado.")
        
    
    aluno1 = {"nome": "Adriel", "nota1": 7, "nota2": 4}
    print(verificar_aluno(aluno1))

######################################################

#EXERCÍCIO 4 - RESUMO DO PRODUTO:

def dicionario4():

    def resumo_produto(produto):
        
        precototal = ((produto["preco"] * produto["quantidade"]))
        return(f"O produto {produto['nome']} contém {produto['quantidade']} em estoque, totalizando R${precototal: ,} ")
    
    produtos = [

        {"nome": "Notebook", "preco": 2500, "quantidade": 200},
        {"nome": "Tablet", "preco": 1700, "quantidade": 100},
        {"nome": "iPhone", "preco": 5000, "quantidade": 250},
        {"nome": "Playstation 5", "preco": 4500, "quantidade": 10}
    ]

    for produto in produtos:
        print(resumo_produto(produto))

dicionario4()