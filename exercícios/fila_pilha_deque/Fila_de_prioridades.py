from ..packages.pilha_e_fila.fila import Queue

def ordenacao(atividade):
    return atividade[1], atividades.index(atividade)


entrada = input().split()
atividades_feitas = int(input())

atividades = [(entrada[i], int(entrada[i+1])) for i in range(0, len(entrada), 2)]
atividades_ordenadas = sorted(atividades, key=ordenacao)


fila_de_atividades = Queue()


for i in range(atividades_feitas, len(atividades_ordenadas)):
    fila_de_atividades.enqueue(atividades_ordenadas[i])



print(f'Tamanho da fila: {fila_de_atividades.size()}')

for i in range(fila_de_atividades.size()):
    atividade = fila_de_atividades.peek(i)
    print(f'Atividade: {atividade[0]}, Prioridade: #{atividade[1]}')