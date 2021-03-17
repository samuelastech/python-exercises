"""-----------------------------------------------------------------------------
LISTA DE EXERCICIOS – INTROD. PROG. ESTRUTURADA – 2020/2
CURSO: Ciencia da Computação – CAMPUS: Chacara Sto. Antônio
PROFESSOR: Vinicius Heltai - DATA: Outubro/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – SEMESTRE: 2º Semestre
ENUNCIADO: 06 - Fazer um algoritmo que calcule e escreva a soma dos
50 primeiros termos das seguintes séries:
100/1 + 997/2 + 994/3 + 991/4
   -----------------------------------------------------------------------------
"""
print("SOMA DOS 50 PRIMEIROS TERMOS")

count = 1
for i in range(1000, 1000-(3*50), -3):
    print(f"{i}/{count} = {i/count:.2f}")
    count += 1