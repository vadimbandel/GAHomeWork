import LibraryGA
import MyGA
import ReadFromFile
import requests


def MakeFormat(answer):
    weight = 0
    volume = 0
    items = []
    for i in range(0, len(answer[1])):
        if answer[1][i] == 1:
            items.append(i + 1)
            weight += ReadFromFile.inputData[i][0]
            volume += ReadFromFile.inputData[i][1]
    return {
        'value': int(answer[0]),
        'weight': int(weight),
        'volume': int(volume),
        'items': items
    }


answer = {
    '1': MakeFormat(LibraryGA.GetLibraryResult()),
    '2': MakeFormat(MyGA.GetMyResult())
}

req = requests.post('https://cit-home1.herokuapp.com/api/ga_homework', json=answer)
print(req.text)
