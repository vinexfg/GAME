

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.level = 1
        self.xp = 0
        self.vida = 100
        self.forca = 10
        self.defesa = 5
        self.inventario = []

    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        if self.xp >= 100:
            self.subir_de_nivel()
    
    def subir_de_nivel(self):
        self.level += 1
        self.xp = 0
        self.vida += 20
        self.forca += 5
        self.defesa += 3
        print(f'{self.nome} subiu para o nivel {self.level}!')

    def atacar(self, inimigo):
        dano = self.forca - inimigo.defesa
        if self.vida <= 0:
            self.vida = 0
            print(f'{self.nome} foi derrotado!')





    
