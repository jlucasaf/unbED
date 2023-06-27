class Node:
    def __init__(self, initData):
        self.data = initData
        self.dir = self.esq = None
    def getData(self):
        return self.data
    
    def get_dir(self):
        return self.dir
    
    def get_esq(self):
        return self.esq
    

class ArvoreBinaria:
    def __init__(self):
        self.root = None
        self.travessia = []

    
    def __search__(self, item, raiz):

        if raiz:
            if item == raiz.data:
                return True
            if item > raiz.getData():
                return self.__search__(item, raiz.dir)
            else:
                return self.__search__(item, raiz.esq)
        return False
    
    def __insert__(self, raiz, no):
        if not raiz:
            return no
        
        if no.getData() > raiz.getData():
            raiz.dir = self.__insert__(raiz.dir, no)
        else:
            raiz.esq = self.__insert__(raiz.esq, no)
        
        return raiz
    
    def __travessia_pos__(self, node):
        if node:
            self.__travessia_pos__(node.esq)
            self.__travessia_pos__(node.dir)
            self.travessia.append(node.data)

    def __travessia_in__(self, node):
        if node:
            self.__travessia_in__(node.esq)
            self.travessia.append(node.data)
            self.__travessia_in__(node.dir)

    def __travessia_pre__(self, node):
        if node:
            self.travessia.append(node.data)
            self.__travessia_pre__(node.esq)
            self.__travessia_pre__(node.dir)
    
    def __imprimir_travessia__(self):
        print(' '.join(str(f) for f in self.travessia))
        self.travessia.clear()

    def insert(self, item):
        no = Node(item)
        self.root = self.__insert__(self.root, no)

    def travessia_pos(self):
        self.__travessia_pos__(self.root)
        self.__imprimir_travessia__()

    def travessia_in(self):
        self.__travessia_in__(self.root)
        self.__imprimir_travessia__()

    def travessia_pre(self):
        self.__travessia_pre__(self.root)
        self.__imprimir_travessia__()

    def search(self, item):
        return self.__search__(item, self.root)