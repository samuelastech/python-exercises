"""-----------------------------------------------------------------------------
LISTA DE EXERCICIOS – INTROD. PROG. ESTRUTURADA – 2020/2
CURSO: Ciencia da Computação – CAMPUS: Chacara Sto. Antônio
PROFESSOR: Vinicius Heltai - DATA: Outubro/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – SEMESTRE: 2º Semestre
ENUNCIADO: 04 – Escreva um procedimento que receba um número arábico
inteiro e imprima o corresponde número em romano. Por exemplo, para 5
a saída desejada é “V”. A função deve ser capaz de gerar o número romano
para os 50 primeiros inteiros. Uma mensagem de erro deve ser mostrada
caso um número fora dessa faixa seja recebido. Crie também um algoritmo
que leia um valor inteiro e chame o procedimento criado acima para a
impressão do número romano.
   -----------------------------------------------------------------------------
"""
print("CONVERSOR PARA NÚMERO ROMANO")
def printNumber(): # Função que imprimi o número inteiro convertido
    control = True
    while control: # Verificação de entrada. Se number > 50, então print("Erro")
        number = int(input("Digite um número inteiro: "))
        if number > 50:
            print("Erro: o número digitado não pode ser maior que 50.\n")
        elif number == 0:
            print("O número", number, "é igual a nulla (nenhum, em romano)\n")
            control = False
        else: # Uma vez feita a validação, é chamada a função convertsToRoman e printado o resultado
            romanNumber = convertsToRoman(number)
            print(f"O número {number} equivale à {romanNumber} em romano")
            control = False

def convertsToRoman(value): # Função que converte árabico para romano
    romanValues = [50, 40, 10, 9, 5, 4, 1]
    romanDigits = ["L", "XL", "X", "IX", "V", "IV", "I"]
    convertedNumber = ''
    for i in range(len(romanValues)):
        while value >= romanValues[i]:
            value -= romanValues[i]
            convertedNumber += romanDigits[i]
    return convertedNumber

printNumber()