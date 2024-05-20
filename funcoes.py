import json

CAMINHO_ARQUIVO = 'Familia.json'
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('vinicius', 22)
p2 = Pessoa('Luana', 21)
p3 = Pessoa('Alice', 2)

bd = [vars(p1), p2.__dict__, vars(p3)]

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii= False, indent=2)
