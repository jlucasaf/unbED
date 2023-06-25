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


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty list."
        tmp = self.head
        lstr = ''
        while tmp != None:
            lstr += str(tmp.data) + ' '
            tmp = tmp.getNext()

        return lstr

    def isEmpty(self):
        return self.head is None

    def addInFront(self, item):  # adiciona no inicio da lista.
        temp = Node(item)
        temp.setNext(self.head)
        temp.setPrevious(None)
        if self.size() > 1:
            self.head.previous = temp
        self.head = temp

    def addInFinal(self, item):
        if self.isEmpty():
            self.addInFront(item)
            return

        temp = Node(item)
        current = self.head
        while current.getNext() is not None:
            current = current.getNext()

        current.next = temp
        temp.previous = current
        temp.next = None

    def addInPosition(self, item, position):

        if position > self.size() or position < 0:
            return

        if position == 0:
            self.addInFront(item)
            return

        if position == self.size():
            self.addInFinal(item)
            return

        temp = Node(item)

        current = self.head
        for i in range(position):
            current = current.getNext()

        # defino as referencias do temp
        temp.previous = current.getPrevious()
        temp.next = current

        temp.getPrevious().next = temp

    def removeFirst(self):
        if self.isEmpty():
            return None

        if self.size() == 1:
            return None

        self.head = self.head.getNext()
        self.head.previous = None

    def removeLast(self):
        if self.isEmpty():
            return None
        if self.size() == 1:
            return None

        current = self.head
        while current.getNext() is not None:
            current = current.getNext()

        current.getPrevious().next = None

    def removeItem(self, item):
        if self.isEmpty():
            return

        if not self.search(item):
            return
        pos = 0
        temp = self.head
        while temp.getData() is not item:
            temp = temp.getNext()
            pos += 1

        if not pos:
            return self.removeFirst()

        if pos == self.size():
            return self.removeLast()

        temp.getNext().previous = temp.previous
        temp.getPrevious().next = temp.next

        return self.head

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


list = ListaDuplamenteEncadeada()

print(list.isEmpty())
list.addInFinal(2)
list.addInFinal(3)
list.addInFinal(4)
list.addInFront(8)
print(list)

list.addInPosition(15, 2)

print(list)
list.removeFirst()
print(list)
list.removeLast()
print(list)
list.removeItem(35)
print(list)
