"""-----------------------------------------------------------------------------
LISTA DE EXERCICIOS – INTROD. PROG. ESTRUTURADA – 2020/2
CURSO: Ciencia da Computação – CAMPUS: Chacara Sto. Antônio
PROFESSOR: Vinicius Heltai - DATA: Outubro/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – SEMESTRE: 2º Semestre
ENUNCIADO: 16 – Elabore um programa que faça a conversão de moedas.
O programa deve receber uma quantidade em determinada moeda e a taxa
de conversão e apresentar a quantidade convertida na moeda selecionada.
Conversões possíveis: dólar para real, euro para real, real para dólar
e real para euro. (utilizar laço de repetição com opção de saída do sistema).
   -----------------------------------------------------------------------------
"""
import textwrap
print("CONVERSOR DE MOEDA")

def converterCoin(price, value): # Faz o processamento da conversão
    priceToConverter = price # Recebe a cotação atual de uma moeda para a outra
    newValue = value * priceToConverter
    return newValue

def translateCoin(type, value): # Função que escolhe a moeda a ser convertida e printa o resultado
    if type == 1: # Dólar
        coinTo = int(input(textwrap.dedent("""
            Para qual moeda deseja converter?
            1 - Real (R$)
            2 - Euro (€)
            Re: """)))

        if coinTo == 1:
            newValue = converterCoin(5.74, value)
            print(f"O valor $ {value:.2f} convertido equivale a R$ {newValue:.2f}")

        elif coinTo == 2:
            newValue = converterCoin(0.85, value)
            print(f"O valor $ {value:.2f} convertido equivale a R$ {newValue:.2f}")
    elif type == 2: # Real
        coinTo = int(input(textwrap.dedent("""
            Para qual moeda deseja converter?
            1 - Dólar ($)
            2 - Euro (€)
            Re: """)))

        if coinTo == 1:
            newValue = converterCoin(0.18, value)
            print(f"O valor R$ {value:.2f} convertido equivale a $ {newValue:.2f}")

        elif coinTo == 2:
            newValue = converterCoin(0.15, value)
            print(f"O valor R$ {value:.2f} convertido equivale a € {newValue:.2f}")

    elif type == 2: # Euro
        coinTo = int(input(textwrap.dedent("""
            Para qual moeda deseja converter?
            1 - Real (R$)
            2 - Dólar ($)
            Re: """)))

        if coinTo == 1:
            newValue = converterCoin(1.17, value)
            print(f"O valor R$ {value:.2f} convertido equivale a $ {newValue:.2f}")

        elif coinTo == 2:
            newValue = converterCoin(6.71, value)
            print(f"O valor R$ {value:.2f} convertido equivale a € {newValue:.2f}")

control = True
while control: # Menu com laço de repetição
    coinType = int(input(textwrap.dedent("""
        Qual a moeda do valor que deseja converter?
        1 - Dólar ($)
        2 - Real (R$)
        3 - Euro (€)
        Digite '0' para sair
        Re: """)))
    if coinType == 0:
        control = False
    coinValue = float(input("\nDigite o valor a ser convertido: "))
    translateCoin(coinType, coinValue)
