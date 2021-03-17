"""-----------------------------------------------------------------------------
LISTA DE EXERCICIOS – INTROD. PROG. ESTRUTURADA – 2020/2
CURSO: Ciencia da Computação – CAMPUS: Chacara Sto. Antônio
PROFESSOR: Vinicius Heltai - DATA: Outubro/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – SEMESTRE: 2º Semestre
ENUNCIADO: 17 – Desenvolver um programa que calcule a média
aritmética simples das notas de um aluno com opção de escolha para
entrada de 2 notas, 3 notas ou 4 notas. Exiba no final o nome do
aluno e sua média com a informação: “Aprovado” se média maior ou igual
a 7, “Reprovado” se média menor que 4 e “Exame” nos demais casos.
(utilizar laço de repetição com opção de saída do sistema).
   -----------------------------------------------------------------------------
"""
import textwrap
print("SISTEMA DE NOTAS")

def averageStudent(qtdEntry):
    name = input("Digite o nome do aluno: ")
    entryList = []
    for i in range(1, qtdEntry+1):
        currentEntry = float(input(f"Digite a {i}ª nota do aluno: "))
        entryList.append(currentEntry)
    average = (sum(entryList))/len(entryList)
    if average >= 7:
        print(f"Aluno: {name}\nMédia: {average}\nSituação: APROVADO")
    elif average < 4:
        print(f"Aluno: {name}\nMédia: {average}\nSituação: REPROVADO")
    else:
        print(f"Aluno: {name}\nMédia: {average}\nSituação: EXAME")
control = True
while control:
    choice = int(input(textwrap.dedent("""
        De quantas notas deseja tirar a média?
        - Duas notas (2)
        - Três notas (3)
        - Quatro notas (4)
        Digite '0' para sair
        Re: """)))

    if choice == 0:
        control = False
    averageStudent(choice)