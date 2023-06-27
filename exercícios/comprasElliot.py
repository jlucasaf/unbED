class ComprasElliot:
    def __init__(self):
        self.lista = []

    def __remove__(self, item):
        item = item[2:]
        index = 0
        while self.lista[index][0] != item:
            index += 1
        self.lista.pop(index)

    def __imprime__(self):
        self.lista.sort(key=lambda x: float(x[1]), reverse=True)
        for i in self.lista:
            print(f'{i[0]}: R$ {float(i[1]):.2f}')

    def __total__(self):
        total = 0
        print("-"*22)
        for i in self.lista:
            total += float(i[1])
        print(f'{len(self.lista)} item(ns): R$ {total:.2f}')
    def listar(self):
        while (item := input()) != "fim":
            if item[0] == "-":
                self.__remove__(item)
            else:
                self.lista.append(item.split())

        self.__imprime__()
        self.__total__()


elliot = ComprasElliot()
elliot.listar()
