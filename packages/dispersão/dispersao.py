class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.tabela_de_dispersao = [None for i in range(size)]

    def __dispersao__(self, chave):
        result = 0
        for i in str(chave):
            result += ord(i)  # retorna o valor da tabela ASCII, não retorna o valor esperado
        return result % len(self.tabela_de_dispersao)

    def insere_dado(self, chave, valor):
        i = self.__dispersao__(chave)
        index = 0

        # caso não exista um vetor, cria um vetor e dar um append em valores que caíram na mesma chave
        if not self.tabela_de_dispersao[i]:
            self.tabela_de_dispersao[i] = []
        # percorre a lista procurando pela chave
        for j, [c, v] in enumerate(self.tabela_de_dispersao[i]):
            if c == chave:
                # se a chave já existe, atualiza o valor correspondente
                self.tabela_de_dispersao[i][j][1] = valor
                return
        # se a chave não existe, adiciona uma nova entrada
        self.tabela_de_dispersao[i].append([chave, valor])

    def ler_dado(self, chave):
        i = self.__dispersao__(chave)
        if self.tabela_de_dispersao[i]:
            for c, v in self.tabela_de_dispersao[i]:
                if c == chave:
                    return v
        raise ValueError("Não possui valor para a chave citada")

    def retira_dado(self, chave):
        i = self.__dispersao__(chave)
        if self.tabela_de_dispersao[i]:
            for c, v in self.tabela_de_dispersao[i]:
                if c == chave:
                    self.tabela_de_dispersao[i].remove([c, v])
                    if not len(self.tabela_de_dispersao[i]):
                        self.tabela_de_dispersao[i] = None
        else:
            raise ValueError("Não existe valor salvo para essa chave")

    def __str__(self):
        return f"{self.tabela_de_dispersao}"