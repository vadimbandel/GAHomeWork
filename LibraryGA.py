from pyeasyga import pyeasyga
import ReadFromFile

# решение на основе: http://pythonhosted.org/pyeasyga/examples.html#multi-dimensional-knapsack-problem
ga = pyeasyga.GeneticAlgorithm(ReadFromFile.inputData)  # initialise the GA with data


# define a fitness function
def Fitness(individual, data):
    weight = 0
    volume = 0
    price = 0
    for selected, item in zip(individual, data):
        if selected:
            weight += item[0]
            volume += item[1]
            price += item[2]
        if weight > ReadFromFile.maxWeight or volume > ReadFromFile.maxVolume:
            price = 0
    return price


ga.fitness_function = Fitness  # set the GA's fitness function
ga.run()  # run the GA

def GetLibraryResult():
    return ga.best_individual()

