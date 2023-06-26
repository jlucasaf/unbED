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
    
    def peek(self, itemPos):
        aux = self.head
        if itemPos - 1 > self.size():
            return None
        for i in range(itemPos):
            aux = aux.getNext()

        return aux.getData()
    
    def get_items(self):
        items = []
        
        if size := self.size():
            aux = self.head
            for i in range(size):
                items.append(aux)
                aux = aux.getNext()
            
            return items
        
        return items
    
    def search(self, item):
        current = self.head
        found = False
        if current.getData() == item:
            return True
        else:
            current = current.getNext()

        while current != self.head and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found
    
    def firstItem(self):
        if not self.size: 
            return None
        return self.head.getData()
    
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
            return

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

    def removeFirst(self):
        if self.isEmpty():
            return None
        
        dado = self.head.getData()

        if self.size() == 1:
            
            self.head = None
            return dado

        previous = self.head.previous
        self.head = previous.next = self.head.next
        self.head.previous = previous
        return dado

    def removeLast(self):
        if self.isEmpty():
            return None
        
        dado = self.head.getPrevious().getData()

        if self.size() == 1:
            self.head = None
            return dado

        last = self.head.previous
        previousLast = last.previous
        self.head.previous = previousLast
        previousLast.next = self.head

        return dado

    def removeItem(self, item):
        if self.isEmpty():
            return None

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

