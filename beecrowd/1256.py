# roda em 0.452s

class HashTable:

    def __init__(self):
        self.tabela = []
        self.casos = 0
        self.enderecos = []
        self.numero_chaves = []
        self.chaves = []

    def numeroCasos(self):
        self.casos = int(input())
        self.tabela = [None] * self.casos
        for i in range(self.casos):
            self.enderecosEChaves(i)
            self.getChaves()
            self.insereNaTabela(i)
        self.printSaida()

    def enderecosEChaves(self, casoTeste):
        entrada = input().split()
        self.enderecos.append(entrada[0])
        self.numero_chaves.append(entrada[1])
        self.tabela[casoTeste] = [None] * int(self.enderecos[casoTeste])

    def getChaves(self):
        self.chaves = input().split()

    def __funcaoDeDispersao__(self, chave, casoTeste):
        return chave % int(self.enderecos[casoTeste])

    def insereNaTabela(self, casoTeste):
        for i in range(len(self.chaves)):
            _hash = self.__funcaoDeDispersao__(int(self.chaves[i]), casoTeste)
            if not self.tabela[casoTeste][_hash]:
                self.tabela[casoTeste][_hash] = []
            self.tabela[casoTeste][_hash].append(self.chaves[i])

    def printSaida(self):
        for j in range(self.casos):
            line = ""
            for i in range(len(self.tabela[j])):
                line = str(i) + " -> "
                if self.tabela[j][i]:
                    for k in range(len(self.tabela[j][i])):
                        line += self.tabela[j][i][k] + " -> "

                line += "\\"
                print(line)
            if j < self.casos - 1:
                print("")


hm = HashTable()

hm.numeroCasos()
