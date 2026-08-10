class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentarnome(self):
        print(f"Olá, meu nome é {self.nome}")

    def apresentaridade(self):
        print(f"E tenho {self.idade} anos!")

pessoa1 = Pessoa("Adriel", 23)
pessoa1.apresentarnome()
pessoa1.apresentaridade()