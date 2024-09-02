

class Itens:
    def __init__(self):
        self.itens_por_elemento = {
            'fogo': [],
            'agua': [],
            'terra': [],
            'ar': []
        }
        
    def adicionar_item(self, elemento, item):
        if elemento in self.itens_por_elemento:
            self.itens_por_elemento[elemento].append(item)
        else:
            print('Elemento invalido!')

    

        