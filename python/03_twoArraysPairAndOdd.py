"""-----------------------------------------------------------------------------
LISTA DE EXERCICIOS – INTROD. PROG. ESTRUTURADA – 2020/2
CURSO: Ciencia da Computação – CAMPUS: Chacara Sto. Antônio
PROFESSOR: Vinicius Heltai - DATA: Outubro/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – SEMESTRE: 2º Semestre
ENUNCIADO: 03 – Escreva uma classe que leia um vetor de 30 posições de
números inteiros e imprimir, logo após, gerar 2 vetores a partir dele,
um contendo os elementos de posições ímpares do vetor e o outro os elementos
pares. Imprimi-los no final.
   -----------------------------------------------------------------------------
"""
import random
print("30 NÚMEROS ALEATÓRIOS")
print("-"*25)
numbers = []

control = 0
while control < 30: # Gerando uma lista aleatória sem números repetidos
    num = random.randrange(1, 101)
    if not num in numbers:
        numbers.append(num)
        control += 1
numbers.sort()

print("Números pares:")
pairList = []
for i in range(len(numbers)): # Verificando os números pares da lista
    if numbers[i] % 2 == 0:
        print("- ", numbers[i])
        pairList.append(numbers[i])
print("São", len(pairList), "números pares\n")

oddList = []
for i in range(len(numbers)): # Verificando os números ímpares da lista
    if numbers[i] % 2 != 0:
        print("- ", numbers[i])
        oddList.append(numbers[i])
print("São", len(oddList), "números ímpares")