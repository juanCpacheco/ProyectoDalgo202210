import sys


def desarrollo(matriz, vis):
    visitados=vis
    cuantos=0
    llaves= matriz.keys()
    for llave in llaves:
        if visitados[llave]==False:
            cuantos+=1
            visitados[llave]=True
            listaAdyacencia= matriz[llave]
            listaAdy(listaAdyacencia,visitados,matriz)
        else:
            pass
    print(cuantos)

def listaAdy(lista, visitados, matriz):
     for elemento in lista:
        if visitados[elemento]==False:
            visitados[elemento]=True
            listaAdy(matriz[elemento],visitados,matriz)


numero_casos = int(sys.stdin.readline())
for __ in range(numero_casos):
    infy=-1
    case_list = list(map(int, sys.stdin.readline().split()))
    vis={}
    matriz={}
    for n in range (len(case_list)):
        actual=int(case_list[n])
        if n==0:
            matriz[actual]= []
            vis[actual]=False
        else :
            matriz[actual]= []
            vis[actual]=False
            i = n-1
            while i > -1:
                anterior=int(case_list[i])
                if anterior>actual:
                    vis[actual]=True
                    pos1=matriz[actual]
                    pos1.append(anterior)
                    pos=matriz[anterior]
                    pos.append(actual)
                i-=1
    desarrollo(matriz,vis)