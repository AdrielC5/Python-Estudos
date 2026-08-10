class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos!")

pessoa1 = Pessoa("Adriel", 23)
pessoa1.apresentar()

pessoa2 = Pessoa("Beatriz Alexandre", 23)
pessoa2.apresentar()

class Animal:

    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print(f"{self.nome} está fazendo um som!")

class Cachorro(Animal):

    def latir(self):
        print(f"{self.nome} está latindo! Au Au")

class Gato(Animal):

    def miar(self):
        print(f"{self.nome} está miando! Miauuuu")

cachorro1 = Cachorro("Rex")
cachorro1.fazer_som()
cachorro1.latir()

gato1 = Gato("Frajola")
gato1.fazer_som()
gato1.miar()