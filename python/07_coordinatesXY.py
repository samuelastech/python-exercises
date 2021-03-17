"""-----------------------------------------------------------------------------
LISTA DE EXERCICIOS – INTROD. PROG. ESTRUTURADA – 2020/2
CURSO: Ciencia da Computação – CAMPUS: Chacara Sto. Antônio
PROFESSOR: Vinicius Heltai - DATA: Outubro/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – SEMESTRE: 2º Semestre
ENUNCIADO: 07 - Escrever um algoritmo que lê um par de coordenadas
(x,y) inteiras e imprima uma mensagem informando em qual quadrante
está o ponto. O algoritmo deve também ser capaz de identificar se o
ponto está sobre um dos eixos ou no ponto central.
   -----------------------------------------------------------------------------
"""
import random

print("COORDENADAS X, Y")
print("-"*20)

#Declaração das Dimensões
coordinateX = int(input("Digite a largura (X): "))
coordinateY = int(input("Digite a altura (Y): "))

INIT = 0 #Constante do início das dimensões

centerPoint = [coordinateX/2, coordinateY/2] #Armazena o ponto central das Dimensões digitada pelo usuário

#Gera uma posição X, Y aleatória dentro das dimensões estabelecidas pelo usuário
pointCordinateX = random.randrange(INIT, coordinateX)
pointCordinateY = random.randrange(INIT, coordinateY)

#Prints de Teste
print(f"\nPonto central (X): {centerPoint[0]:.0f}\nPonto central (Y): {centerPoint[1]:.0f}\n")
print(f"Onde o ponto está? X: {pointCordinateX} Y: {pointCordinateY}")

if pointCordinateX < centerPoint[0] and pointCordinateY < centerPoint[1]:
    print("O ponto está no QUADRANTE 1")
elif pointCordinateX > centerPoint[0] and pointCordinateY < centerPoint[1]:
    print("O ponto está no QUADRANTE 2")
elif pointCordinateX < centerPoint[0] and pointCordinateY > centerPoint[1]:
    print("O ponto está no QUADRANTE 3")
elif pointCordinateX > centerPoint[0] and pointCordinateY > centerPoint[1]:
    print("O ponto está no QUADRANTE 4")
elif pointCordinateX == centerPoint[0] and pointCordinateY == centerPoint[1]:
    print("O ponto está no CENTRO DAS DIMENSÕES")
elif pointCordinateX == centerPoint[0] and pointCordinateY == centerPoint[1]:
    print("O ponto está no CENTRO DAS DIMENSÕES")
elif pointCordinateX == centerPoint[0] and pointCordinateY != centerPoint[1]:
    print("O ponto está no CENTRO DO EIXO X")
elif pointCordinateX != centerPoint[0] and pointCordinateY == centerPoint[1]:
    print("O ponto está no CENTRO DO EIXO Y")