

class Pessoa:

    atributo = 'valor'
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return 2024 - self.idade
    
p1 = Pessoa('vinicius', 22)
p2 = Pessoa('Luana', 21)


print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())