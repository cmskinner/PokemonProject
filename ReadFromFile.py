'''

'''

import statistics

dataFile = [line.rstrip() for line in open('data.txt')]

print(dataFile)

data = []

for eachNumber in dataFile:
    data.append(float(eachNumber))

print(data)

mean = statistics.mean(data)
mode = statistics.mode(data)

print(mean)
print(mode)

listOfIndex = []
counter = 0
for eachNumber in data:
    counter += 1
    if(eachNumber > mean):
        listOfIndex.append(int(counter))

print(listOfIndex)

dataFile2 = [line.rstrip() for line in open('Pokemon.txt')]
print(dataFile2)
pokemon = []

counter2 = 0
for eachString in dataFile2:
    pokemon.append(str(eachString))
    counter2 += 1

higherPower = []
for eachNumber in listOfIndex:
    higherPower.append(pokemon[eachNumber - 1])

print(higherPower)

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