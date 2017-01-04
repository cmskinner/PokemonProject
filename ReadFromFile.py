'''

'''

import statistics

dataFile = [line.rstrip() for line in open('data.txt')]

data = []

for eachNumber in dataFile:
    data.append(float(eachNumber))

mean = statistics.mean(data)

listOfIndex = []
counter = 0
for eachNumber in data:
    counter += 1
    if(eachNumber > mean):
        listOfIndex.append(int(counter))

dataFile2 = [line.rstrip() for line in open('Pokemon.txt')]
pokemon = []

counter2 = 0
for eachString in dataFile2:
    pokemon.append(str(eachString))
    counter2 += 1

higherPower = []
for eachNumber in listOfIndex:
    higherPower.append(pokemon[eachNumber - 1])

createFile = open('AboveAveragePowerPokemon.txt', 'w')
createFile.close

appendFile = open('AboveAveragePowerPokemon.txt', 'a')

writeToFileList = []
theLength = len(higherPower)
n = 0
while n < theLength:
    appendFile.write('' + str(listOfIndex[n]) +
                           ': ' + str(higherPower[n]) + '\n')
    n += 1

appendFile.close