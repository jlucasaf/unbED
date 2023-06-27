from .packages.pilha_e_fila.pilha import Stack

pilha = Stack()

while (entrada := int(input())) != 0:
    pilha.push(entrada)

item = int(input())

pesoTotal = 0
anilhasRetiradas = 0
peso = 0
if pilha.search(item):
    while (peso := pilha.pop()) != item:
        pesoTotal = pesoTotal + peso
        anilhasRetiradas = anilhasRetiradas + 1
        print(f'Peso retirado: {peso}')
    print(f'Peso retirado: {peso}')
    print(f'Anilhas retiradas: {anilhasRetiradas + 1}')
    print(f'Peso total movimentado: {pesoTotal + peso}')