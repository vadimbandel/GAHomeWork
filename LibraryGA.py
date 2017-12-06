from pyeasyga import pyeasyga

# решение на основе: http://pythonhosted.org/pyeasyga/examples.html#multi-dimensional-knapsack-problem

# читаем данные из файла в список кортежей
inputData = [tuple(map(float, i.split(' '))) for i in open('data.txt').readlines()]

maxWeight = inputData[0][0]
maxVolume = inputData[0][1]

inputData.remove(inputData[0])

ga = pyeasyga.GeneticAlgorithm(inputData)  # initialise the GA with data


# define a fitness function
def fitness(individual, data):
    weight = 0
    volume = 0
    price = 0
    for selected, item in zip(individual, data):
        if selected:
            weight += item[0]
            volume += item[1]
            price += item[2]
        if weight > maxWeight or volume > maxVolume:
            price = 0
    return price


ga.fitness_function = fitness  # set the GA's fitness function
ga.run()  # run the GA


def makeFormat(fitness_result):
    weight = 0
    volume = 0
    items = []
    for i in range(0, len(fitness_result[1])):
        if fitness_result[1][i] == 1:
            items.append(i + 1)
            weight += inputData[i][0]
            volume += inputData[i][1]
    return int(fitness_result[0]), int(weight), round(volume), items


def getResult():
    return makeFormat(ga.best_individual())
