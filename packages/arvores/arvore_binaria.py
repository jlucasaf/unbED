class Node:
    def __init__(self, initData):
        self.data = initData
        self.dir = self.esq = None


class ArvoreBinaria:
    def __init__(self):
        self.root = None

    def insert(self, raiz,  item):
        aux = Node(item)

        if not raiz:

            return aux

        if aux.data > raiz.data:
            raiz.dir = self.insert(raiz.dir, item)
        else:
            raiz.esq = self.insert(raiz.esq, item)

        return raiz

    def travessia_pos(self, node):
        if node:
            self.travessia_pos(node.esq)
            self.travessia_pos(node.dir)
            print(node.data)
    def travessia_in(self, node):
        if node:
            self.travessia_in(node.esq)
            print(node.data)
            self.travessia_in(node.dir)

    def travessia_pre(self, node):
        if node:
            print(node.data)
            self.travessia_pre(node.esq)
            self.travessia_pre(node.dir)



arvore = ArvoreBinaria()

arvore.root = arvore.insert(arvore.root, 5)
arvore.root = arvore.insert(arvore.root, 4)
arvore.root = arvore.insert(arvore.root, 7)
arvore.root = arvore.insert(arvore.root, 3)

arvore.travessia_in(arvore.root)
print("/" * 10)
arvore.travessia_pos(arvore.root)
print("/" * 10)
arvore.travessia_pre(arvore.root)
