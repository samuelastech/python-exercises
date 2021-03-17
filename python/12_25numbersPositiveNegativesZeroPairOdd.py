"""-----------------------------------------------------------------------------
LISTA DE EXERCICIOS – INTROD. PROG. ESTRUTURADA – 2020/2
CURSO: Ciencia da Computação – CAMPUS: Chacara Sto. Antônio
PROFESSOR: Vinicius Heltai - DATA: Outubro/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – SEMESTRE: 2º Semestre
ENUNCIADO: 12 - Desenvolva um programa que receba 25 números (tipo float)
digitados pelo usuário e apresente no final a quantidade de números
positivos, negativos, zeros, pares e ímpares digitados.
   -----------------------------------------------------------------------------
"""
print("25 NÚMEROS: POSTIVOS, NEGATIVOS, ZEROS, PARES E ÍMPARES")
numberList = []
positiveNumbers = []
negativeNumbers = []
zeroNumbers = []
pairNumbers = []
oddNumbers = []

for i in range(1, 3): # Entrada de Dados
    number = float(input(f"Digite um número ({i}): "))
    numberList.append(number)

def checkNumber(value): # Função para verificar a natureza do número
    if value % 2 == 0: # Número PAR
        if value > 0:
            positiveNumbers.append(value)
            pairNumbers.append(value)
        elif value < 0:
            negativeNumbers.append(value)
            pairNumbers.append(value)
        elif value == 0:
            zeroNumbers.append(value)
    else: # Número ÍMPAR
        oddNumbers.append(value)
        if value > 0:
            positiveNumbers.append(value)
        elif value < 0:
            negativeNumbers.append(value)
        else:
            zeroNumbers.append(value)

'''
    Loop para percorrer o vetor definido pelo usuário e que chama 
    a função para defnir a natureza do número
'''
for i in range(len(numberList)):
    checkNumber(numberList[i])
else:
    print(f"\nNúmeros POSITIVOS: {len(positiveNumbers)}")
    print(f"Números NEGATIVOS: {len(negativeNumbers)}")
    print(f"Números PARES: {len(pairNumbers)}")
    print(f"Números ÍMPARES: {len(oddNumbers)}")
    print(f"ZEROS: {len(zeroNumbers)}")