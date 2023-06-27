def encontra_virus(amostra):
    for l, linha in enumerate(amostra):
        for c, valor in enumerate(linha):
            if valor == 0:
                return l, c
    return None

def virus_esta_aniquilado(amostra, linha, coluna):

    if amostra[linha - 1][coluna] != 1:
        return False
    if amostra[linha + 1][coluna] != 1:
        return False
    if amostra[linha][coluna + 1] != 1:
        return False
    if amostra[linha][coluna - 1] != 1:
        return False

    return True

formato_amostra = input().split()
amostra = []

for i in range(int(formato_amostra[0])):
    linha = []
    for j in (linha_string := input().split()):
        linha.append(int(j))
    amostra.append(linha)



linha, coluna = encontra_virus(amostra)

virus_aniquilado = virus_esta_aniquilado(amostra, int(linha), int(coluna))

if virus_aniquilado:
    print(f'{linha} {coluna}')
else:
    print("0 0")


