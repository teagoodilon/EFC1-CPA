#Lucas Neves Sáber Gabriel - 202020459 - 10A
#Thiago Odilon de Almeida - 202021025 - 10A
#Otávio Augusto Trindade Fonseca - 202020551 - 10A
def calculo(n, x, y, matutina, vespertina):
    custos = []
    matutina = [int(x) for x in matutina]
    vespertina = [int(x) for x in vespertina]
    for i in range(n):
        tHoras = min(matutina) + max(vespertina)
        matutina.remove(min(matutina))
        vespertina.remove(max(vespertina))
        if (tHoras - x) > 0:
            excedente = (tHoras - x) * y
        else:
            excedente = 0
        custos.append(excedente)
    print(sum(custos))

while True:
    n, x, y = map(int, input().split())
    if n == 0 and x == 0 and y == 0:
        break
    duracaoMatutinas = input().split()
    duracaoVespertinas = input().split()
    calculo(n, x, y, duracaoMatutinas , duracaoVespertinas)