#Lucas Neves Sáber Gabriel - 202020459 - 10A
#Thiago Odilon de Almeida - 202021025 - 10A
#Otávio Augusto Trindade Fonseca - 202020551 - 10A
cont = 0
def mergeSort(vetor):
    if len(vetor) <= 1:
        return vetor
    meio = len(vetor) // 2
    esquerda = mergeSort(vetor[:meio])
    direita = mergeSort(vetor[meio:])
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    global cont 
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
            cont += len(esquerda) - i
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

while True:
    try:
        cont = 0
        n, *seq = map(int, input().split())
        mergeSort(seq)
        if cont % 2 == 0:
            print("Eder")
        else:
            print("Wando")
    except EOFError:
        break