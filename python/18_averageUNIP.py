"""-----------------------------------------------------------------------------
LISTA DE EXERCICIOS – INTROD. PROG. ESTRUTURADA – 2020/2
CURSO: Ciencia da Computação – CAMPUS: Chacara Sto. Antônio
PROFESSOR: Vinicius Heltai - DATA: Outubro/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – SEMESTRE: 2º Semestre
ENUNCIADO: 18 – Desenvolver um programa que entre com as notas (NP1
e NP2), quantidade de falta e carga horaria da disciplina e informe
se o aluno “Passou Direto”, “Exame”, “Substitutiva” ou “Reprovado”.
Caso o aluno entre com “NC” o aluno deve realizar a PSUB. Caso o
aluno fique com nota insatisfatória, deve realizar um exame e após o
lançamento, o programa deve reanalisar a situação, acrescentando
“Aprovado após exame” ou “Reprovado após exame”. A regra deve ser a
mesma do Manual do Aluno (vide páginas 14 e 25) disponível no link:
https://unip.br/presencial/servicos/aluno/download/calendario_manual_cursos_tradicionais1.pdf
   -----------------------------------------------------------------------------
"""
import textwrap
print("SISTEMA DE NOTAS - UNIP")

def averageCheck(average, studentData, np): # Checa a média do aluno para tomar as decisões
    studentData.append(float(np[0]))
    studentData.append(float(np[1]))

    if average >= 6.7 and average < 7:
        average = 7
    studentData.append(average)
    if average >= 7:
        situation = "APROVADO DIRETO"
        studentData.append(situation)
        printStatistic(studentData)
    elif average < 6.7:
        exam = float(input("Digite a nota do EXAME: "))
        finalAverage = (average + exam) / 2
        if average >= 4.75 and average < 5:
            finalAverage = 5
        if average >= 5 or average < 5:
            situation = "APROVADO PÓS EXAME"
            studentData.append(situation)
            studentData.append(exam)
            studentData.append(finalAverage)
            printStatistic(studentData)
            if average < 5:
                situation = "REPROVADO PÓS EXAME"
                printStatistic(studentData)

def studentSituation(): # Recebe as informações do Estudante e faz as validações
    name = input("\nDigite o nome do Aluno: ")
    frequency = int(input("Digite a quantidade de faltas do aluno: "))
    workload = int(input("Digite a carga horária da disciplina no semestre: "))
    percentageFrequency = 100 - (frequency / workload) * 100

    studentData = [name, frequency, percentageFrequency]

    if percentageFrequency < 75:
        situation = "REPROVADO POR FALTA"
        studentData.append(situation)
        printStatistic(studentData)
    else:
        np1 = input("Entre com a nota da NP1: ")
        np2 = input("Entre com a nota da NP2: ")
        npList = [np1, np2]

        if np1 == "NC" and np2 == "NC":
            situation = "REPROVADO POR NÃO COMPARECER AS PROVAS"
            studentData.append(situation)
            printStatistic(studentData)
        elif np1 == "NC":
            psub = float(input("Digite a nota da Prova Substitutiva (NP1): "))
            newNpList = [psub, np2]
            semiannualAverage = (psub + float(npList[1])) / 2
            averageCheck(semiannualAverage, studentData, newNpList)
        elif "NC" in npList[1]:
            psub = float(input("Digite a nota da Prova Substitutiva (NP2): "))
            newNpList = [np2, psub]
            semiannualAverage = (psub + float(npList[0])) / 2
            averageCheck(semiannualAverage, studentData, newNpList)
        else:
            semiannualAverage = (float(np1) + float(np2)) / 2
            averageCheck(semiannualAverage, studentData, npList)

def printStatistic(data): # Printa o resultado final do estudante
    if len(data) == 4: # REPROVADO POR FALTA OU POR NÃO COMPARECER AS PROVAS
        print(textwrap.dedent(f"""
            Aluno: {data[0]}
            Faltas: {data[1]} | Frequência: {data[2]:.1f} %
            Situação: {data[3]}"""))

    elif len(data) == 7: # PASSOU DIRETO
        print(data)
        print(textwrap.dedent(f"""
            Aluno: {data[0]}
            NP1: {data[3]:.1f} | NP2: {data[4]:.1f}
            MS: {data[5]:.1f}
            Faltas: {data[1]} | Frequência: {data[2]:.1f} %
            Situação: {data[6]}"""))

    elif len(data) == 9: # EXAME
        print(textwrap.dedent(f"""
            Aluno: {data[0]}
            NP1: {data[3]:.1f} NP2: {data[4]:.1f}
            MS: {data[5]:.1f} Exame: {data[7]:.1f} MF: {data[8]}
            Faltas: {data[1]} | Frequência: {data[2]:.1f} %
            Situação: {data[6]}"""))

control = True
while control: # MENU COM OPÇÃO DE SAÍDA
    choice = int(input(textwrap.dedent(f"""
        1 - Situação Aluno
        2 - Sair...
        Re: """)))
    if choice == 1:
        studentSituation()
    else:
        control = False