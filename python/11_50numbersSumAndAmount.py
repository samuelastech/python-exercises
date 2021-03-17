"""-----------------------------------------------------------------------------
LISTA DE EXERCICIOS – INTROD. PROG. ESTRUTURADA – 2020/2
CURSO: Ciencia da Computação – CAMPUS: Chacara Sto. Antônio
PROFESSOR: Vinicius Heltai - DATA: Outubro/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – SEMESTRE: 2º Semestre
ENUNCIADO: 11 – Construa um programa que, para um grupo de 50 valores
inteiros, determine:
a) A soma dos números positivos;
b) A quantidade de valores negativos.
   -----------------------------------------------------------------------------
"""
import random
print("50 NÚMEROS INTEIROS: SOMA DOS POSITIVOS E QUANTIDADE DE NEGATIVOS")

numberList = []
for i in range(50): # Armazena valores positivos e negativos no Vetor
    numberList.append(random.randrange(-101, 101))
else:
    positiveNumbers = []
    negativeNumbers = []
    for j in range(len(numberList)): # Percorre o Vetor e armazena, em novas listas, os números positivos e negativos
        if numberList[j] > 0:
            positiveNumbers.append(j)
        else:
            negativeNumbers.append(j)

    print(f"Lista com 50 números:\n{numberList}")
    print(f"A soma dos números positivos é igual: {sum(positiveNumbers)}")
    print(f"A quantidade de números negativos é igual: {len(negativeNumbers)}")