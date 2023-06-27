class TinderDonaFlorinda:
    def __init__(self):
        self.listaPretendente = []
        self.ALTURA = 2
        self.PESO = 3
        self.NOME = 0
        self.SOBRENOME = 1
        self.PESO_IDEAL = 75
        self.ALTURA_IDEAL = 180

    def pegaPretendente(self):
        for i in range(int(input())):
            self.listaPretendente.append(input().split())

    def __key_de_ordenacao__(self, candidato):
        dif_altura = abs(int(candidato[self.ALTURA]) - self.ALTURA_IDEAL)
        peso_ideal = int(candidato[self.PESO]) == self.PESO_IDEAL
        menor_peso = int(candidato[self.PESO])
        sobrenome = self.SOBRENOME
        nome = self.NOME
        return dif_altura, peso_ideal, menor_peso, sobrenome, nome

    def ordenaPretendente(self):
        self.listaPretendente.sort(key=self.__key_de_ordenacao__)

    def mostraPrentendente(self):
        for candidato in self.listaPretendente:
            print(f'{candidato[self.SOBRENOME]}, {candidato[self.NOME]}')

donaFlorinda = TinderDonaFlorinda()
donaFlorinda.pegaPretendente()
donaFlorinda.ordenaPretendente()
donaFlorinda.mostraPrentendente()