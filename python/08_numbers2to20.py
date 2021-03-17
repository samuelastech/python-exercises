"""-----------------------------------------------------------------------------
LISTA DE EXERCICIOS – INTROD. PROG. ESTRUTURADA – 2020/2
CURSO: Ciencia da Computação – CAMPUS: Chacara Sto. Antônio
PROFESSOR: Vinicius Heltai - DATA: Outubro/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – SEMESTRE: 2º Semestre
ENUNCIADO: 08 - Crie um programa que leia um número entre 2 e 20 e
gere uma tela com a seguinte configuração:

Digite um número: 7
Saída do programa:
1234567
x123456
xx12345
xxx1234
xxxx123
xxxxx12
xxxxxx1
   -----------------------------------------------------------------------------
"""
print("-"*25)
length = int(input("Digite um número: "))
numberList = []

for i in range(length, 0, -1): # Loop que inicia com o valor máximo digitado
    numberOutput = ''
    xAmount = length - i # Definindo a qtd de 'x' a ser printada
    x = "x" * xAmount

    for j in range(1, i+1): # Segundo loop que fatora e concatena os números em um str
        numberOutput += str(j)
    numberOutput = x + numberOutput #Acrescenta-se a qtd de 'x'
    numberList.append(numberOutput)

for i in range(len(numberList)): # Print na tela
    print(numberList[i])