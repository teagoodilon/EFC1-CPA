import random

def InsertionSort(A):
  for j in range(1, len(A)):
    chave = A[j]
    i = j-1
    while i >= 0 and A[i] > chave:
      A[i+1] = A[i]
      i = i - 1
    A[i+1] = chave

vetor1 = random.sample(range(-15, -5), 5)
vetor2 = random.sample(range(-4, 5), 5)
vetor3 = random.sample(range(6, 15), 5)

InsertionSort(vetor1)
InsertionSort(vetor2)
InsertionSort(vetor3)

print("Vetor 1 ordenado = ", vetor1)
print("Vetor 2 ordenado = ", vetor2)
print("Vetor 3 ordenado = ", vetor3)