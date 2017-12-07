# читаем данные из файла в список кортежей
inputData = [tuple(map(float, i.split(' '))) for i in open('data.txt').readlines()]
maxWeight = inputData[0][0]
maxVolume = inputData[0][1]
inputData.remove(inputData[0])