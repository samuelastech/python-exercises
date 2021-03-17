"""-----------------------------------------------------------------------------
LISTA DE EXERCICIOS – INTROD. PROG. ESTRUTURADA – 2020/2
CURSO: Ciencia da Computação – CAMPUS: Chacara Sto. Antônio
PROFESSOR: Vinicius Heltai - DATA: Outubro/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – SEMESTRE: 2º Semestre
ENUNCIADO: Escrever um algoritmo que produza na tela um triângulo de
Pascal de grau “n” usando uma matriz. Abaixo temos um triângulo de
Pascal de grau 6 (isto é, com seis linhas):

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1

Os elementos extremos em cada linha são iguais a 1. Os outros são
obtidos somando-se os dois valores que aparecem imediatamente acima e à
esquerda na linha anterior. Exemplo: O quarto elemento da linha
corresponde a soma do quarto e do terceiro elemento na linha anterior,
isto é, 4 = 1 + 3.
   -----------------------------------------------------------------------------
"""

print("TRIÂNGULO DE PASCAL")
length = int(input("Digite o grau do triângulo: "))
triangle = []

for rowIndex in range(length+1): # Linha
    rowValues = [] # Uma nova linha vazia
    for columnIndex in range(rowIndex): # Coluna
        if rowIndex == 0: # Se for a primeira linha, colocamos "1"
            rowValues.append(1)

        elif columnIndex == 0 or columnIndex == rowIndex-1: # Verificando se o primeiro e último elemento da lista são diferente de um
            rowValues.append(1)

        else:
            previousRow = rowIndex - 1 # Obtendo Índice da linha anterior
            previousColumn = columnIndex - 1 # Obtendo valor da coluna da esquerda

            value = triangle[previousRow][previousColumn] + triangle[previousRow][columnIndex]
            
            rowValues.append(value)

    triangle.append(rowValues) # Armazena a linha na Matriz

for pascalLine in range(length+1): # Exibe o triângulo na tela
    print(triangle[pascalLine])
