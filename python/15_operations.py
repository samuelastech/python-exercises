"""-----------------------------------------------------------------------------
LISTA DE EXERCICIOS – INTROD. PROG. ESTRUTURADA – 2020/2
CURSO: Ciencia da Computação – CAMPUS: Chacara Sto. Antônio
PROFESSOR: Vinicius Heltai - DATA: Outubro/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – SEMESTRE: 2º Semestre
ENUNCIADO: 15 – Elabore um programa que receba dois números (tipo float)
digitados pelo usuário e pergunte qual operação ele deseja realizar.
Operações possíveis: soma, subtração, multiplicação, divisão, maior e menor
número. Exiba no final os números digitados e o resultado da operação escolhida.
   -----------------------------------------------------------------------------
"""
import textwrap

print("CALCULADORA")
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

choice = int(input(textwrap.dedent("""
    Que operação você quer realizar?
    1. Soma (+)
    2. Subtração (-)
    3. Multiplicação (×)
    4. Divisão (÷)
    5. Maior (>)
    6. Menor (<)
    Re: """)))

if choice == 1:
    print(f"\nNúmero 1: {num1}\nNúmero 2: {num2}\n{num1} + {num2} = {num1 + num2}")
elif choice == 2:
    print(f"\nNúmero 1: {num1}\nNúmero 2: {num2}\n{num1} - {num2} = {num1 - num2}")
elif choice == 3:
    print(f"\nNúmero 1: {num1}\nNúmero 2: {num2}\n{num1} × {num2} = {num1 * num2}")
elif choice == 4:
    print(f"\nNúmero 1: {num1}\nNúmero 2: {num2}\n{num1} ÷ {num2} = {num1 * num2}")
elif choice == 5:
    print(f"\nNúmero 1: {num1}\nNúmero 2: {num2}\nO número {max(num1, num2)} é o maior")
elif choice == 6:
    print(f"\nNúmero 1: {num1}\nNúmero 2: {num2}\nO número {min(num1, num2)} é o menor")