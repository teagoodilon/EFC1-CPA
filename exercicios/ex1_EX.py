#Lucas Neves Sáber Gabriel - 202020459 - 10A
#Thiago Odilon de Almeida - 202021025 - 10A
#Otávio Augusto Trindade Fonseca - 202020551 - 10A
def calculo(n, x):
    solucoesParciais = [0] * (n+1)
    solucoesParciais[0] = 1
    for i in range(1, x+1):
        for j in range(1, n+1):
            solucoesParciais[j] = (solucoesParciais[j] + solucoesParciais[j-1]) % 1000000
    return solucoesParciais[n]

while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    print(calculo(n, x))