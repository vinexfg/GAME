import json


CAMINHO_DO_ARQUIVO = 'ARMAZEN'

class Cliente:
    def __init__(self,nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    
    def coletar_dados(self):
        print('Foneça seus dados conforme como pedido. ')
        self.nome = input('Nome: ')
        self.sobrenome = input('Sobrenome: ')
        self.idade = int(input('Idade: '))

    def to_dict(self):
        return{
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'idade': self.idade,
        }
    
def salvar_dados(cliente):
    dados_do_cliente = cliente.to_dict()
    with open('cliente_dados.json', 'w') as arquivo_json:
        json.dump(dados_do_cliente, arquivo_json, indent= 4)

cliente = Cliente(nome= '', sobrenome = '', idade=0)
cliente.coletar_dados()

salvar_dados(cliente)
print('Dados do cliente armazrnados com sucecco em "cliente_dados.json"')
        
    