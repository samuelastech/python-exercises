"""-----------------------------------------------------------------------------
LISTA DE EXERCICIOS – INTROD. PROG. ESTRUTURADA – 2020/2
CURSO: Ciencia da Computação – CAMPUS: Chacara Sto. Antônio
PROFESSOR: Vinicius Heltai - DATA: Outubro/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – SEMESTRE: 2º Semestre
ENUNCIADO: 13 - Desenvolva um programa que receba nome, idade e salário
digitados pelo usuário e apresente no final quantas dessas idades estão
entre 15 e 17 anos, quantas são maiores de 21 anos, quantos salários estão
entre R$1.500,00 e R$2.000,00, quantos estão acima de R$3.500,00 e qual é
o maior e o menor salário digitado. (utilizar laço de repetição com opção
de saída do sistema).
   -----------------------------------------------------------------------------
"""
import textwrap
print("ANÁLISE DE USUÁRIOS")
print("-"*20)
userList = []

'''Função que printa os resultados da análise de dados'''
def printAnalysis(ageDetail1, ageDetail2, salaryDetail1, salaryDetail2, salaryDetail3):
    print(textwrap.dedent(f"""
        1. A quantidade de idades entre 15 e 17 anos é: {len(ageDetail1)};
        2. A quantidade de idades maiores que 21 anos é: {len(ageDetail2)};
        3. A quantidade de salários entre R$ 1.500,00 e R$ 2.000,00 é: {len(salaryDetail1)};
        4. A quantidade de salários maiores que R$ 3.500,00 é: {len(salaryDetail2)}
        5. O maior salário cadastrado é: {max(salaryDetail3)}, e o menor: {min(salaryDetail3)}.
    """))

'''Função que faz a análise de dados'''
def userAnalysis(): #
    ageList = []
    salaryList = []
    for i in range(len(userList)):
        ageList.append(userList[i][1])
        salaryList.append(userList[i][2])

    ageDetail1 = [] # Vetor com a qtd de idades entre 15 e 17 anos
    ageDetail2 = [] # Vetor com a qtd de idades maior que 21 anos
    salaryDetail1 = [] # Vetor com a qtd de salários entre R$1.500,00 e R$2.000,00
    salaryDetail2 = [] # Vetor com a qtd de salários acima de R$3.500,00
    for j in range(len(ageList)):
        if ageList[j] >= 15 and ageList[j] <= 17:
            ageDetail1.append(ageList[j])
        elif ageList[j] > 21:
            ageDetail2.append(ageList[j])

    for z in range(len(salaryList)):
        if salaryList[z] >= 1500 and salaryList[z] <= 2000:
            salaryDetail1.append(salaryList[z])
        elif salaryList[z] > 3500:
            salaryDetail2.append(salaryList[z])

    printAnalysis(ageDetail1, ageDetail2, salaryDetail1, salaryDetail2, salaryList)

'''Função que cadastra os usuários'''
def registerUser():
    name = input("\nDigite o nome do usuário: ")
    age = int(input("Digite a a idade do usuário: "))
    salary = float(input("Digite o salário do usuario: "))
    user = [name, age, salary]
    userList.append(user)

'''Menu do Programa'''
control = True
count = 0
while control:
    choice = int(input(textwrap.dedent(f"""
        Usuários cadastrados {count}
        
        - Cadastrar usuário (1)
        - Sair (2)
        
        O que deseja fazer? (int): """)))

    if choice == 1:
        registerUser()
        count += 1

        if count > 1:
            userAnalysis()
    elif choice == 2:
        control = False