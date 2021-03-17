"""-----------------------------------------------------------------------------
LISTA DE EXERCICIOS – INTROD. PROG. ESTRUTURADA – 2020/2
CURSO: Ciencia da Computação – CAMPUS: Chacara Sto. Antônio
PROFESSOR: Vinicius Heltai - DATA: Outubro/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – SEMESTRE: 2º Semestre
ENUNCIADO: 14 – Desenvolva um programa que receba nome e salário de
um funcionário e calcule o valor do salário líquido desse funcionário,
utilizando função, descontando os impostos INSS e Imposto de Renda (IR)
conforme tabela oficial vigente. (utilizar laço de repetição com opção
de saída do sistema).
   -----------------------------------------------------------------------------
"""
import textwrap
print("FUNCIONÁRIOS")

def checkEmployee():
    employeeName = input("\nDigite o nome do funcionário: ")
    employeeSalary = float(input("Digite o salário do funcionário: "))
    cashSalary = []

    '''Descontando o INSS'''
    if employeeSalary <= 1045:
        inssAliquot = 0.075

        salary = employeeSalary - (employeeSalary * inssAliquot)
        cashSalary.append(salary)

    elif employeeSalary >= 1045.01 and employeeSalary <= 2089.60:
        inssAliquot = 0.09

        salary = employeeSalary - (employeeSalary * inssAliquot)
        cashSalary.append(salary)

    elif employeeSalary >= 2089.61 and employeeSalary <= 3134.40:
        inssAliquot = 0.12

        salary = employeeSalary - (employeeSalary * inssAliquot)
        cashSalary.append(salary)

    elif employeeSalary >= 3134.41 and employeeSalary <= 6101.06:
        inssAliquot = 0.14

        salary = employeeSalary - (employeeSalary * inssAliquot)
        cashSalary.append(salary)

    '''Descontando o IRPF'''
    if employeeSalary >= 1903.99 and employeeSalary <= 2826.65:
        irpfAliquot = 0.075

        newSalary = cashSalary[0] - (cashSalary[0] * irpfAliquot)
        print(f"O novo salário do funcionário é R$ {newSalary:.2f}")

    elif employeeSalary >= 2826.66 and employeeSalary <= 3751.05:
        irpfAliquot = 0.15

        newSalary = cashSalary[0] - (cashSalary[0] * irpfAliquot)
        print(f"O novo salário do funcionário é R$ {newSalary:.2f}")

    elif employeeSalary >= 3751.05 and employeeSalary <= 4664.68:
        irpfAliquot = 0.225

        newSalary = cashSalary[0] - (cashSalary[0] * irpfAliquot)
        print(f"O novo salário do funcionário é R$ {newSalary:.2f}")

    elif employeeSalary > 4664.69:
        irpfAliquot = 0.275

        newSalary = cashSalary[1] - (cashSalary[1] * irpfAliquot)
        print(f"O novo salário do funcionário é R$ {newSalary:.2f}")

control = True
while control:
    choice = int(input(textwrap.dedent("""
        - Verificar funcionário (1)
        - Sair (2)
        
        O que deseja fazer? (int): """)))

    if choice == 1:
        checkEmployee()
    elif choice == 2:
        control = False