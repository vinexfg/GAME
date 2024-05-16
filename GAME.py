from random import randint

lista_npcs = []


player ={
    'nome': 'vinicius',
    'level': 1,
    'exp': 0,
    'expMax': 50,
    'hp': 100,
    'hpMax': 100,
    'dano': 25


}


def criar_npcs():
    level = randint(0, 60)
    novo_npcs = {
        'nome': f'ARK #{level}', 
        'level': level,
        'dano': level,
        'hp': 100 * level,
        'exp': 7 * level
        }
    lista_npcs.append(novo_npcs)

def gerar_npcs(qtd_npc):
    for x in range(qtd_npc):
        criar_npcs()

def exibir_npcs():
    for npc in lista_npcs:
        print(f'Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // HP: {npc['hp']} ')


#atacar_npc(npc) - npc:hp - plaver:dano
def atacar_npc(npc):
    npc['hp'] -= player['dano']
#atacar_player(npc) - player:hp - npc:dano

qtd_de_npcs = 5     
criar_npcs()
gerar_npcs(qtd_de_npcs)
exibir_npcs()


npc_selecionado = lista_npcs[0]

print(f'NPC para atacar: {npc_selecionado}')

