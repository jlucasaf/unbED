class Palindromo:
    def __init__(self):
        self.palavras = []
        self.palidromo1 = []
        self.result = []

    def pegaPalavras(self):
        self.palavras = input().split()

    def verificaPalindromo(self, inicio, fim, palavra):
        palavra_ordem_certa = palavra[inicio:fim]
        palavra_invertida = palavra_ordem_certa[::-1]
        if palavra_ordem_certa == palavra_invertida:
            return inicio, fim, palavra_ordem_certa

        return False

    def armazenaPalindromo(self, inicio, fim, palavra):
        if palindromo := self.verificaPalindromo(inicio, fim, palavra):
            self.palidromo1.append(palindromo)

    def encontraTodosOsPalindromoNaPalavra(self,pos):
        len_palavra = len(self.palavras[pos])
        for i in range(len_palavra):
            for j in range(i + 3, len_palavra + 1):
                self.armazenaPalindromo(i,j,self.palavras[pos])

    def verificaSeTemIguais(self):
        new_palindromo = []
        for i, tupla1 in enumerate(self.palidromo1):
            is_equal = False
            for j, tupla2 in enumerate(self.palidromo1):
                if i != j and tupla1[2] == tupla2[2]:
                    is_equal = True
            if not is_equal:
                new_palindromo.append(tupla1)
        self.palidromo1 = new_palindromo

    def verificaSeTemContidos(self):
        new_palindromo = []
        for i, tupla1 in enumerate(self.palidromo1):
            is_contido = False
            for j, tupla2 in enumerate(self.palidromo1):
                if i != j and tupla1[0] >= tupla2[0] and tupla1[1] <= tupla2[1]:
                    is_contido = True
                    break
            if not is_contido:
                new_palindromo.append(tupla1)
        self.palidromo1 = new_palindromo

    def verificaSeEh2Palindromo(self, pos):
        self.encontraTodosOsPalindromoNaPalavra(pos)
        self.verificaSeTemContidos()
        self.verificaSeTemIguais()
        length = len(self.palidromo1)
        if length >= 2:
            self.result.append((self.palavras[pos], True))
        else:
            self.result.append((self.palavras[pos], False))

    def palindromar(self):
        result = ""
        self.pegaPalavras()
        length = len(self.palavras)
        for i in range(length):
            self.palidromo1 = []
            self.verificaSeEh2Palindromo(i)
        for i in self.result:
            if i[1]:
                result += i[0] + " "

        print(result)


palindromo = Palindromo()
palindromo.palindromar()
