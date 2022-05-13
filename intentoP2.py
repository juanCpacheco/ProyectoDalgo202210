import sys

numero_casos = int(sys.stdin.readline())
for caso in range(numero_casos):
    case_list = list(map(int, sys.stdin.readline().split()))
    visitados = []
    componentes = []
    cant = 0
    for i in range(len(case_list)):
        actual = case_list[i]
        if actual not in visitados:
            visitados.append(actual)
            componente = []
            componente. append(actual)
            for j in range(i+1, len(case_list)):
                actual2 = case_list[j]
                if actual > actual2 and actual2 not in visitados:
                    componente.append(actual2)
                    visitados.append(actual2)
            componentes.append(componente)
    # print(componentes)
    print(len(componentes))
