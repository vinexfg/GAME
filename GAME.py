from random import randint

list_npcs = []


player = {
    'Nome': 'vinicius',
    'level': '1',
    'exp': '0',
    'expMax': '50',
    'hp': '100',
    'hpMax': '100',
    'damege': '25',
}


def create_npcs():
    level = randint(0, 60)
    novo_npcs ={
        'name': 'ARK',
        'level': level,
        'damege': level,
        'hp': '100' * level,
        'exp': 7 * level,

    }
    
    list_npcs.append(novo_npcs)

def generate_npcs(amount_npc):
    for x in range(amount_npc):
        create_npcs()

def exibir_npcs():
    for npc in list_npcs:
        print(f'Name: {npc['name']} // Level: {npc['level']} // Damege: {npc['damege']} // Hp: {npc['hp']}')

def atacar_npc(npc):
    npc['hp'] -= player['dano']


number_of_npc = 5
create_npcs()
generate_npcs(number_of_npc)
exibir_npcs()

select_npc = list_npcs[0]

print(f'Npc to attack: {select_npc}')

