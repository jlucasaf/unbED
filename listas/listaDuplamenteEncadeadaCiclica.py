class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.previous = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrevious(self, newPrevious):
        self.previous = newPrevious


class ListaDuplamenteEncadeadaCiclica:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty list."
        tmp = self.head
        lstr = ''
        lstr += str(tmp.data) + ' '
        tmp = tmp.getNext()

        while tmp != self.head:
            lstr += str(tmp.data) + ' '
            tmp = tmp.getNext()

        return lstr

    def isEmpty(self):
        return self.head is None

    def addInFront(self, item):  # adiciona no inicio da lista.
        temp = Node(item)
        if self.isEmpty():
            self.head = temp
            self.head.next = self.head
            self.head.previous = self.head
            return

        if self.size() == 1:
            temp.next = temp.previous = self.head
            self.head.previous = self.head.next = temp
            self.head = temp

            return

        temp.next = self.head
        temp.previous = self.head.previous
        self.head.previous = temp
        temp.previous.next = temp
        self.head = temp

    def addInFinal(self, item):
        if self.isEmpty():
            return self.addInFront(item)

        temp = Node(item)
        if self.size() == 1:
            self.head.next = self.head.previous = temp
            temp.previous = temp.next = self.head

        temp.next = self.head
        temp.previous = self.head.previous
        self.head.previous = temp
        temp.previous.next = temp

    def addInPosition(self, item, pos):
        print(self.size())
        if pos > self.size() or pos < 0:
            return

        if not pos:
            self.addInFront(item)
            return

        if pos == self.size():
            self.addInFinal(item)
            return

        temp = Node(item)

        current = self.head
        for i in range(pos):
            current = current.getNext()

        # defino as referencias do temp
        temp.previous = current.getPrevious()
        temp.next = current

        temp.getPrevious().next = temp

    def size(self):
        if self.isEmpty():
            return 0

        current = self.head
        count = 0
        count = count + 1
        current = current.getNext()
        while current != self.head:
            count = count + 1
            current = current.getNext()

        return count


listaCiclica = ListaDuplamenteEncadeadaCiclica()

listaCiclica.addInFront(2)
print(listaCiclica)
listaCiclica.addInFront(3)
print(listaCiclica)
listaCiclica.addInFront(4)
print(listaCiclica)
listaCiclica.addInFinal(8)
print(listaCiclica)
listaCiclica.addInPosition(10, 4)
print(listaCiclica)
