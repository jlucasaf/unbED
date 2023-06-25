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

    def addInFinal(self, item):
        temp = Node(item)
        aux = self.head
        while aux.getNext() is not None:
            aux = aux.getNext()

        aux.next = temp

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
    
    def removeFirst(self):
        if self.head:
            current = self.head
            if self.head.getNext():
                self.head = self.head.getNext()
            else:
                self.head = None
            
            return current.getData()
        

    def peek(self, itemIndex):
        aux = self.head
        if itemIndex - 1 > self.size():
            return None
        for i in range(itemIndex):
            aux = aux.getNext()

        return aux.getData()

    def clear(self):
        self.head = None

    def get_items(self):
        auxList = []
        aux = self.head
        for i in range(self.size()):
            auxList.append(aux.getData)
            aux = aux.getNext
        return auxList


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
