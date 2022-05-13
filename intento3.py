import sys

numero_casos = int(sys.stdin.readline())
for caso in range(numero_casos):
    case_list = list(map(int, sys.stdin.readline().split()))
    cant = 0
    while len(case_list) > 0:
        actual = case_list[0]
        case_list.remove(actual)
        j = 0
        while j < len(case_list):
            actual2 = case_list[j]
            if actual > actual2:
                case_list.remove(actual2)
            else:
                j += 1
        cant += 1

    # print(componentes)
    print(cant)
