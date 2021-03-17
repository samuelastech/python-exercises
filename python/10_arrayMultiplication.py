"""-----------------------------------------------------------------------------
LISTA DE EXERCICIOS – INTROD. PROG. ESTRUTURADA – 2020/2
CURSO: Ciencia da Computação – CAMPUS: Chacara Sto. Antônio
PROFESSOR: Vinicius Heltai - DATA: Outubro/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – SEMESTRE: 2º Semestre
ENUNCIADO: 10 – Elabore um algoritmo que leia dois vetores de dez
posições e faça a multiplicação dos elementos da seguinte forma:
o primeiro do vetor 1 com o último do vetor 2, o segundo do vetor
1 com o penúltimo do vetor 2 e assim por diante, colocando o resultado
num terceiro vetor, que deve ser mostrado como saída.
   -----------------------------------------------------------------------------
"""
import random

print("MULTIPLICAÇÃO DE VETORES DE 10 POSIÇÕES")
vector1 = []
vector2 = []
vectorProduct = []

for i in range(10):
    vector1.append(random.randrange(1, 100))
    vector2.append(random.randrange(1, 100))
else:
    for j in range(10):
        product = vector1[j] * vector2[9-j]
        vectorProduct.append(product)
    print(f"Vetor 1: {vector1}")
    print(f"Vetor 2: {vector2}")
    print(f"Produto invertido dos Vetores: {vectorProduct}")