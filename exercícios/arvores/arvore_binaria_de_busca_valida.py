class ArvoreBinaria():
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir


def constituiArvoreBinariaDeBusca(raiz):
    if raiz:
        if raiz.esq:
            if raiz.esq.dado > raz.dado:
                return 1
    
    return 0


raiz = ArvoreBinaria(2, ArvoreBinaria(1), ArvoreBinaria(3))