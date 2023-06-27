from packages.pilha_e_fila.pilha import Stack

# implemente uma fila usando uma pilha (enqueue dequeue)

class FilaComPilha:
    def __init__(self):
        self.auxPilha = Stack()

    def enqueue(self, item):
        self.auxPilha.push(item)

    def dequeue(self):
        lista = []
        for i in range(self.auxPilha.size() - 1):
            lista.append(self.auxPilha.pop())

        data = self.auxPilha.pop()

        for i in lista[::-1]:
            self.auxPilha.push(i)
        return data
    

fila = FilaComPilha()

fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(5)
fila.enqueue(3)

print(fila.dequeue())
print(fila.dequeue())
print(fila.dequeue())