import sys

numero_casos = int(sys.stdin.readline())
for caso in range(numero_casos):
    case_list = list(map(int, sys.stdin.readline().split()))
    visitados = []
    cant = 0
    for i in range(len(case_list)):
        actual = case_list[i]
        if actual not in visitados:
            visitados.append(actual)
            for j in range(i+1, len(case_list)):
                actual2 = case_list[j]
                if actual > actual2 and actual2 not in visitados:
                    visitados.append(actual2)
            cant += 1
    # print(componentes)
    print(cant)
