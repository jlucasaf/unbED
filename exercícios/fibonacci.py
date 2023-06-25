class Fib:
    def __init__(self):
        self.lista = [0] * 31
        self.result = 0

    def fib(self, n):
        self.lista[n] += 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

    def calcularEPrintar(self):
        numero = int(input())
        self.result = self.fib(numero)
        print(f'fibonacci({numero}) = {self.result}.')
        self.printChamadas(numero)

    def printChamadas(self, n):
        for i in range(n + 1):
            print(f'{self.lista[i]} chamada(s) a fibonacci({i}).')


fibonacci = Fib()
fibonacci.calcularEPrintar()