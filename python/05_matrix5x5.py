"""-----------------------------------------------------------------------------
LISTA DE EXERCICIOS – INTROD. PROG. ESTRUTURADA – 2020/2
CURSO: Ciencia da Computação – CAMPUS: Chacara Sto. Antônio
PROFESSOR: Vinicius Heltai - DATA: Outubro/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – SEMESTRE: 2º Semestre
ENUNCIADO: 05 - Preencher por leitura uma matriz M (5,5). Em seguida,
calcular e imprimir a matriz toda e a média dos elementos das áreas
assinaladas: linha 3 e coluna 2; linha 4, coluna 2 e coluna 3; linha 5,
coluna 2, coluna 3 e coluna 4 (figura do PDF)
   -----------------------------------------------------------------------------
"""
print("MATRIZ 5x5")
matrix = []

for rowIndex in range(1, 6): # Cria a matrix a partir da entrada de dados do usuário
    row = []
    for columnIndex in range(1, 6):
        number = int(input(f"Digite um número para preencher a matriz (linha {rowIndex}, coluna {columnIndex}): "))
        row.append(number)
    matrix.append(row)

numbers = []
for rowIndex in range(2, len(matrix)): # Armazena os elementos específicos da matriz
    for columnIndex in range(1, rowIndex):
        number = matrix[rowIndex][columnIndex]
        numbers.append(number)
average = sum(numbers) / len(numbers)

for i in range(len(matrix)): # Imprimi as linhas da matrix e a média aritimética
    print(matrix[i])
else:
    print(f"A média dos elementos específicos é: {average}")
