class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos!")

    def __str__(self):
        return f"Pessoa chamada {self.nome}"


pessoa1 = Pessoa("Adriel", 23)
pessoa1.apresentar()
print(pessoa1)

pessoa2 = Pessoa("Beatriz Alexandre", 23)
pessoa2.apresentar()

class Animal:

    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print(f"{self.nome} está fazendo um som!")

class Cachorro(Animal):

    def fazer_som(self):
        print(f"{self.nome} está latindo! Au Au")

class Gato(Animal):

    def fazer_som(self):
        print(f"{self.nome} está miando! Miauuuu")

class Passaro(Animal):

    def fazer_som(self):
        print(f"{self.nome} está piando! Piu Piu Piu")

animais = [Cachorro("Rex"), Gato("Frajola"), Passaro("Piu Piu")]

for animal in animais:
    animal.fazer_som()
