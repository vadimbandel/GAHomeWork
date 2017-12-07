import random
import ReadFromFile


def GenerateFirstPopulation(count):
    firstGeneration = []
    for i in range(0, count):
        individ = []
        for i in range(0, len(ReadFromFile.inputData)):
            individ.append(int(round(random.random())))
        firstGeneration.append(individ)
    return firstGeneration


def Fitness(individual, data):
    weight, volume, price = 0, 0, 0
    for (selected, item) in zip(individual, data):
        if selected:
            weight += item[0]
            volume += item[1]
            price += item[2]
    if weight > ReadFromFile.maxWeight or volume > ReadFromFile.maxVolume:
        price = 0
    return price


def Selection(firstPopulation):
    generationAndPrice = []
    for individual in firstPopulation:
        generationAndPrice.append((individual, Fitness(individual, ReadFromFile.inputData)))
        generationAndPrice.sort(key=lambda i: float(i[1]), reverse=True)
    selectedGeneration = []
    for i in range(0, int(len(generationAndPrice) * 0.2)):
        selectedGeneration.append(generationAndPrice[i][0])
    return selectedGeneration

def Crossingover(afterSelection):
    length = len(afterSelection[0])
    children = []
    for p in range(0, len(afterSelection), 2):
        mate1 = afterSelection[p]
        mate2 = afterSelection[p + 1]
        one = random.randint(0, length - 1)
        two = random.randint(one, length - 1)
        three = random.randint(two, length - 1)
        children.append(mate1[:one] + mate2[one:two] + mate1[two:three] + mate2[three:])
        children.append(mate2[:one] + mate1[one:two] + mate2[two:three] + mate1[three:])
    return children

def Mutation(children):
    for i in range(0, int(len(children) * 0.05)):
        ind = random.randint(0, len(children) - 1)
        for j in range(0, 3):
            numberOfBit = random.randint(0, 29)
            children[ind][numberOfBit] = children[ind][numberOfBit] ^ 1
    return children

def NewPopulation(firstPopulation, mutatedPopulation):
    generationAndPrice = []
    for individual in generationAndPrice:
        generationAndPrice.append((individual, Fitness(individual, ReadFromFile.inputData)))
        generationAndPrice.sort(key=lambda i: float(i[1]))
    newPopulation = []
    for i in range(0, len(generationAndPrice)):
        newPopulation.append(generationAndPrice[i][0])
#меняю худшие особи из первоначальных, на все новые после мутации(иначе как можно поменять 30% на 20%?)
    for i in range(0, len(mutatedPopulation)):
        firstPopulation[i] = mutatedPopulation[i]
    return firstPopulation

def GetMax(population):
    generationAndPrice = []
    for individual in population:
        generationAndPrice.append((individual, Fitness(individual, ReadFromFile.inputData)))
    maximum = max(generationAndPrice, key=lambda item: float(item[1]))

    return maximum

def Convergence(firstPopulation, newPopulation):
    firstMax = GetMax(firstPopulation)[1]
    newMax = GetMax(newPopulation)[1]
    return abs(firstMax - newMax) < firstMax*0.1


def GetMyResult():
    firstPopulation = GenerateFirstPopulation(200)
    for i in range(0, 100):
        afterSelection = Selection(firstPopulation)
        afterCrossingover = Crossingover(afterSelection)
        afterMutation = Mutation(afterCrossingover)
        newPopulation = NewPopulation(firstPopulation, afterMutation)
        if not Convergence(firstPopulation, newPopulation):
            firstPopulation = newPopulation
        else:
            answer = GetMax(newPopulation)
            return answer[1], answer[0]