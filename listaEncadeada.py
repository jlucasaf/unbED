class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def __str__(self):
        return f'[{self.data}]'

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

    def setHead(self, item):
        self.head = item

    def setTale(self, item):
        if item.next:
            item.next = None

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

    def getItemByPos(self, pos):
        current = self.head
        previous = None
        for i in range(pos):
            if current.getData():
                if current.getNext():
                    previous = current
                    current = current.getNext()
                else:
                    raise IndexError
            else:
                raise IndexError

        return current


def inverterLista(lista):
    if lista:
        size = lista.size()
        for i in range(size - 1, -1, -1):
            if not i:
                break
            node = lista.getItemByPos(i)
            if new_next := lista.getItemByPos(i - 1):
                node.next = new_next
        lista.setHead(lista.getItemByPos(size))
        lista.setTale(lista.getItemByPos(0))
    return lista


L = UnorderedList()
L.add(1)
L.add(2)
L.add(3)
L.add(4)
L.add(5)

print(L.getItemByPos(3))


print(f'Lista antes: {L}')
L = inverterLista(L)
print(f'Lista depois: {L}')
