import random

def SelectionSort(Array):
  tam = len(Array)
  for i in range(tam):
    menor = i
    for j in range(i + 1, tam):
      if (Array[menor] > Array[j]):
        menor = j
    temp = Array[i]
    Array[i] = Array[menor]
    Array[menor] = temp

vetor1 = random.sample(range(-15, -5), 5)
vetor2 = random.sample(range(-4, 5), 5)
vetor3 = random.sample(range(6, 15), 5)

SelectionSort(vetor1)
SelectionSort(vetor2)
SelectionSort(vetor3)

print("Vetor 1 ordenado = ", vetor1)
print("Vetor 2 ordenado = ", vetor2)
print("Vetor 3 ordenado = ", vetor3)