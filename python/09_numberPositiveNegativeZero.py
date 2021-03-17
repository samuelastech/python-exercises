"""-----------------------------------------------------------------------------
LISTA DE EXERCICIOS – INTROD. PROG. ESTRUTURADA – 2020/2
CURSO: Ciencia da Computação – CAMPUS: Chacara Sto. Antônio
PROFESSOR: Vinicius Heltai - DATA: Outubro/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – SEMESTRE: 2º Semestre
ENUNCIADO: 09 -  Faça uma função que recebe um valor inteiro e verifica
se o valor é positivo, negativo ou zero. A função deve retornar 1 para
valores positivos, ‐1 para negativos e 0 para o valor 0.
   -----------------------------------------------------------------------------
"""

print("NÚMERO POSITIVO, NEGATIVO OU ZERO")
print("(Positivo: 1 | Negativo: -1 | Zero: 0)\n")

def checkNumber(value):
    if value < 0:
        return -1
    elif value > 0:
        return 1
    elif value == 0:
        return 0

def printNumber():
    number = int(input("Digite um número inteiro: "))
    print(checkNumber(number))

printNumber()