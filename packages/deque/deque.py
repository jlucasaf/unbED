from ..listas.listaDuplamenteEncadeadaCiclica import ListaDuplamenteEncadeadaCiclica

class Deque:
    def __init__(self) -> None:
        self.auxList = ListaDuplamenteEncadeadaCiclica()

    def __eq__(self, other) -> bool:
        if isinstance(other, Deque):
            if self.size() == other.size():
                for i in range(self.size()):
                    if self.auxList.peek(i) != other.auxList.peek(i):
                        return False
                return True
            return False
        return False

    def __str__(self) -> str:
        return self.auxList.__str__()

    def is_empty(self):
        return self.auxList.isEmpty()
    
    def size(self):
        return self.auxList.size()
    
    def search(self, item):
        return self.auxList.search(item)
    
    def reverse(self):
        reversedDeque = Deque()
        for i in range(self.auxList.size() - 1, -1, -1):
            reversedDeque.push_back(self.auxList.peek(i))
        return reversedDeque
    
    
    def clear(self):
        self.auxList.head = None

    def front(self):
        if self.auxList.head:
            return self.auxList.head.getData()
        return None
    
    def back(self):
        if aux := self.auxList.head:
            aux = aux.getPrevious().getData()
            return aux
        return None
    
    def push_front(self, item):
        self.auxList.addInFront(item)

    def push_back(self, item):
        self.auxList.addInFinal(item)

    def pop_front(self):
        return self.auxList.removeFirst()
    
    def pop_back(self):
        return self.auxList.removeLast()

    
    