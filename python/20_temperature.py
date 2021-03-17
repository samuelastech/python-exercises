"""-----------------------------------------------------------------------------
LISTA DE EXERCICIOS – INTROD. PROG. ESTRUTURADA – 2020/2
CURSO: Ciencia da Computação – CAMPUS: Chacara Sto. Antônio
PROFESSOR: Vinicius Heltai - DATA: Outubro/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – SEMESTRE: 2º Semestre
ENUNCIADO: 20 – Desenvolva um programa que receba 10 valores de
temperatura ambiente de uma cidade. O programa deve armazenar tais
valores em uma lista denominada temp, conforme os valores vão sendo
recebidos. Após isso, o programa deve retornar a média de temperatura,
temperatura máxima, temperatura mínima e por fim criar uma segunda lista
(chamada dados) e por os valores em ordem crescente.
   -----------------------------------------------------------------------------
"""
import textwrap
print("TEMPERATURA (ºC)")
temp = []

for i in range(1, 10+1):
    currentTem = int(input(f"Digite a {i}ª temperatura ambiente do seu município: "))
    temp.append(currentTem)

print(textwrap.dedent(f"""
A temperatura média desse município é: {sum(temp)/len(temp):.1f}ºC
A temperatura máxima é: {max(temp)}ºC
A temperatura mínima é: {min(temp)}ºC
    """))

data = temp.copy()
data.sort()
print("LISTA COM AS TEMPERATURAS")
for i in range(len(data)):
    print(f"- {data[i]}ºC")