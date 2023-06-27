from ...packages.arvores.arvore_binaria import ArvoreBinaria

arvoreBinariaDeBusca = ArvoreBinaria()



while (entrada := input()) != "quack":
    if entrada == "in":
        arvoreBinariaDeBusca.travessia_in()
    elif entrada == "pre":
        arvoreBinariaDeBusca.travessia_pre()
    elif entrada == "pos":
        arvoreBinariaDeBusca.travessia_pos()
    else:
        arvoreBinariaDeBusca.insert(int(entrada))