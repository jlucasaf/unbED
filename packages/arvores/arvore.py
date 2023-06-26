class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.filhos = []
    
    def insert(self, item):
        self.filhos.append(item)
    
    def remove(self, folha):
        if folha in self.raiz.filhos:
            self.filhos.remove(folha)
    
    def altura(self):
        if self.filhos:
            return 1 + max(f.altura() for f in self.filhos)
        return 0
    
    def ordem_no(self):
        return len(self.filhos)
    
        
    
    

class Arvore:
    def __init__(self, dado):
        self.root = Node(dado)

    def ordem_arvore(self):
        if self.root:

            if self.root.filhos:
                ordem_sub = max(f.ordem_arvore() for f in self.root.filhos)

                return max(self.ordem_no(), ordem_sub)
        
            return 0  
        
        return None

    def busca(self, item):
        if self.root:
            if self.root.data == item:
                return True
            for f in self.root.filhos:
                if f.busca(item):
                    return True
        return False  

    def numero_nos(self):
        if self.root:
            total = 1  

            if self.root.filhos:
                for f in self.root.filhos:
                    total += f.numero_nos()
            return total
        return 0





    



        