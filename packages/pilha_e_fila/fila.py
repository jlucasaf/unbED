from ..listas.listaDuplamenteEncadeadaCiclica import ListaDuplamenteEncadeadaCiclica

class Queue:
    def __init__(self):
        self.auxList = ListaDuplamenteEncadeadaCiclica()

    def __str__(self) -> str:
        return self.auxList.__str__()
    
    def enqueue(self, item):
        self.auxList.addInFinal(item)
    
    def dequeue(self, item):
        return self.auxList.removeFirst()
    
    def peek(self, itemPos):
        return self.auxList.peek(itemPos)
    
    def is_empty(self):
        return self.auxList.isEmpty()
    
    def size(self):
        return self.auxList.size()
    
    def search(self, item):
        return self.auxList.search(item)
    
    def front(self):
        return self.auxList.firstItem()
    
    def get_items(self):
        return self.auxList.get_items()
    
    def clear(self):
        self.auxList.head = None

        
    
