
from packages.listas.listaEncadeada import UnorderedList

class Stack:
    def __init__(self):
        self.auxList = UnorderedList()

    def __str__(self):
        return self.auxList.__str__()

    def push(self, item):
        self.auxList.add(item)
    
    def pop(self):
        return self.auxList.removeFirst()

    def top(self):
        return self.auxList.head.getData()

    def is_empty(self):
        return self.auxList.isEmpty()

    def size(self):
        return self.auxList.size()

    def search(self, item):
        return self.auxList.search(item)

    def peek(self, itemIndex):
        return self.auxList.peek(itemIndex)

    def clear(self):
        return self.auxList.clear()

    def get_items(self):
        return self.auxList.get_items()