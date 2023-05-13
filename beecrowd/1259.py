# roda em 0.376s

linhas = int(input())

pares = []
impares = []

for i in range(linhas):
    numero = int(input())
    if numero % 2:
        impares.append(numero)
    else:
        pares.append(numero)


if pares:
    pares.sort()
    for i in pares:
        print(i)
if impares:
    impares.sort(reverse=True)
    for i in impares:
        print(i)








