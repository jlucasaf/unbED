import numpy as np
class CalculaTempo:
    def __init__(self):
        self.data1 = []
        self.data2 = []
        self.duracao = []
        self.horarios = [0, 0]
        self.tabelaDeTransformacao = [86400, 3600, 60, 1]

    def duracaoTotal(self):
        self.recebeData()
        if self.__verificaData__():
            self.transformaSegundoParaData()

    def recebeData(self):
        self.data1 = input().split()
        self.data2 = input().split()
        self.data1[1] = self.data1[1].split(":")
        self.data2[1] = self.data2[1].split(":")

        self.data1 = [self.data1[0]] + self.data1[1]
        self.data2 = [self.data2[0]] + self.data2[1]


    def __verificaData__(self):
        for i in self.tabelaDeTransformacao:
            index = 0
            self.horarios[0] += int(self.data1[index]) * i
            self.horarios[1] += int(self.data2[index]) * i
            index += 1

        return self.horarios[1] > self.horarios[0]

    def __tempoDeDuracao__(self):
        return self.horarios[1] - self.horarios[0]

    def transformaSegundoParaData(self):
        tempoDuracao = self.__tempoDeDuracao__()
        print(tempoDuracao)
        for i, element in enumerate(self.tabelaDeTransformacao):
            self.duracao.append(tempoDuracao % element)
            tempoDuracao = tempoDuracao - self.duracao[i]
            print(tempoDuracao, self.duracao)




casamentoDuracao = CalculaTempo()

casamentoDuracao.duracaoTotal()
