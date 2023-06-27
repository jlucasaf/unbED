from packages.pilha_e_fila.fila import Queue

class PilhaComFila():
    def __init__(self):
        self.auxFila = Queue()

    def push(self,item):
        self.auxFila.enqueue(item)
    
    def pop(self):
        lista = []
        for i in range(self.auxFila.size() - 1):
            lista.append(self.auxFila.dequeue())

        dado = self.auxFila.dequeue()
        for i in lista:
            self.auxFila.enqueue(i)

        return dado

pilha = PilhaComFila()

pilha.push(1)
pilha.push(3)
pilha.push(4)
pilha.push(7)

print(pilha.pop())
print(pilha.pop())
print(pilha.pop())