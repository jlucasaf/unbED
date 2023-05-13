class Minerador:
    def __init__(self):
        self.aberturas = []
        self.fechamentos = []
        self.casoTeste = 0
        self.minerios = []

    def minerar(self):
        self.casoTeste = int(input())
        self.minerios = [None] * self.casoTeste
        self.aberturas = [0] * self.casoTeste
        self.fechamentos = [0] * self.casoTeste
        for i in range(self.casoTeste):
            self.campoDeMineracao(i)
            self.verificaDimantes(i)
        self.numeroDeDiamantes(self.casoTeste)

    def campoDeMineracao(self, casoTeste):
        self.minerios[casoTeste] = input()

    def verificaDimantes(self, casoTeste):
        for i in self.minerios[casoTeste]:
            if i == "<":
                self.aberturas[casoTeste] += 1
            if i == ">":
                self.fechamentos[casoTeste] += 1
        print(self.aberturas, self.fechamentos)

    def numeroDeDiamantes(self, casoTeste):
        if self.aberturas[casoTeste] <= self.fechamentos[casoTeste]:
            print(self.aberturas[casoTeste])
        elif self.aberturas[casoTeste] > self.fechamentos[casoTeste]:
            print(self.fechamentos[casoTeste])


minerador = Minerador()
minerador.minerar()
