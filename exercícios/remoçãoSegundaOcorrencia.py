class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        tmp = self.head
        lstr = ''
        while tmp != None:
            lstr += str(tmp.data) + ' '
            tmp = tmp.getNext()

        return lstr

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def removeByPosition(self, item, ocorrencia):
        current = self.head
        previous = None
        _ocorrencia = 0
        size = L.size()
        i = 0
        while not ocorrencia == _ocorrencia:

            if current.getData() == item:
                _ocorrencia += 1

                if _ocorrencia != ocorrencia:
                    previous = current
                    current = current.getNext()

            else:
                previous = current
                current = current.getNext()

            i += 1
            if not current:
                return

        if ocorrencia == _ocorrencia:
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())


def removerSegundaOcorrencia(L, n):
    if not L.isEmpty():
        L.removeByPosition(n, 2)
    return L


L = UnorderedList()
L.add(1)
L.add(2)
L.add(3)
L.add(2)
L.add(4)
L.add(2)
L.add(5)
L.add(2)
L.add(6)
L.add(2)
L.add(7)
L = removerSegundaOcorrencia(L, 2)
print(f'Lista: {L}')
