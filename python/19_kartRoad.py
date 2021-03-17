"""-----------------------------------------------------------------------------
LISTA DE EXERCICIOS – INTROD. PROG. ESTRUTURADA – 2020/2
CURSO: Ciencia da Computação – CAMPUS: Chacara Sto. Antônio
PROFESSOR: Vinicius Heltai - DATA: Outubro/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – SEMESTRE: 2º Semestre
ENUNCIADO: 19 – Uma pista de Kart permite 10 voltas para cada um de
6 corredores. Escreva um programa que leia todos os tempos em segundos
e os guarde em um dicionário, onde a chave é o nome do corredor. Ao final
diga de quem foi a melhor volta da prova e em que volta; e ainda a
classificação final em ordem (1o o campeão). O campeão é o que tem a menor
média de tempos.
   -----------------------------------------------------------------------------
"""
import random, operator
print("CORRIDA - 10 VOLTAS")
runners = {}

for runnerIndex in range(1, 6+1): # Loop para coletar o nome do corredor e seus tempos
    runnerName = input(f"{runnerIndex}. Digite o nome do {runnerIndex}º motorista: ")

    # Colet o tempo em cada volta
    runnerTime = {}
    for runnerTurnIndex in range(1,10+1):
        runnerTime.update({f"VOLTA {runnerTurnIndex}": random.uniform(15, 45)})
    runners.update({runnerName: runnerTime})

minTurnList = [] # Lista que armazena o corredor, tempo mínimo e a volta do tempo mínimo
winnerList = [] # Lista que armazena o corredor e a média de tempo final deles
for i in runners: # Iterando o dicionário com os corredores e seus tempos
    name = i # Salvando o nome do corredor
    turnMinTime = min(runners[i].values()) # Salvando o menor tempo dele
    turnIndex = min(runners[i].items(), key=operator.itemgetter(1))[0] # Salvando a volta com o menor tempo dele
    runnerAverage = (sum(runners[i].values())/len(runners[i].values())) # Salvando a média total dele

    bestTurn = name, turnMinTime, turnIndex # Tupla com os critérios "(...) quem foi a melhor volta da prova e em que volta"
    placing = name, runnerAverage # Tupla com os critérios "(...) a classificação final em ordem (1o o campeão)"

    '''Enviando as tuplas para uma lista'''
    minTurnList.append(bestTurn)
    winnerList.append(placing)

'''1º - CRIANDO O RANKING COM OS CAMPEÕES '''
averages = []
for i in range(len(winnerList)):
    averages.append(winnerList[i][1])
averages.sort()

count = 0
print("\nRANKING")
while count <= len(averages)-1:
    subCount = 0
    control = True
    while control:
        if averages[count] == winnerList[subCount][1]:
            print(f"{count+1}º {winnerList[subCount][0]} | Média de tempo: {averages[count]:.2f} s")
            count += 1
            control = False
        else:
            subCount += 1

'''2º - EXIBINDO A MELHOR VOLTA '''
bestTimeList = []
for i in range(len(minTurnList)):
    bestTimeList.append(minTurnList[i][1])

control = True
while control:
    subCount = 0
    while control:
        if min(bestTimeList) == minTurnList[subCount][1]:
            print(f"\n{minTurnList[subCount][2]}, realizada por {minTurnList[subCount][0]}, foi a melhor, com média de: {min(bestTimeList):.2f} s")
            control = False
        else:
            subCount += 1
