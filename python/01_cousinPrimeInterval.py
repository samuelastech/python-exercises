"""-----------------------------------------------------------------------------
LISTA DE EXERCICIOS – INTROD. PROG. ESTRUTURADA – 2020/2
CURSO: Ciencia da Computação – CAMPUS: Chacara Sto. Antônio
PROFESSOR: Vinicius Heltai - DATA: Outubro/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – SEMESTRE: 2º Semestre
ENUNCIADO: 01 - Desenvolva uma classe que apresente todos os números 
primos existentes entre N1 e N2, em que N1 e N2 são números naturais
fornecidos. Um número é primo quando é divisível somente por ele e 
pela unidade (1).
   -----------------------------------------------------------------------------
"""

print("INTERVALO DE NÚMEROS INTEIROS")
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
cousinPrime = 0

for i in range(n1, n2+1): #Loop para percorrer todo o intervalo definido pelo usuário
    div = 0 # Quantidade de divisores que um número possui
    control = True

    while control: #Loop para descobrir a quantidade de divisores do número
        for j in range(1, i+1):
            if i % j == 0: #Se o quociente da divisão for igual a zero, incrementa-se a variável div
                div +=1

            if div > 2: #Caso o número possua mais de dois divisores ele não é primo
                control = False
        
        if div == 2:
            cousinPrime +=1
            print("- ", i)
            control = False
else:
    print("Essa é a quantidade de números primos nesse intervalo: ", cousinPrime)
