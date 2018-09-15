import matplotlib.pyplot as plt
import csv

def printGraph():
    file = open("files/positions.csv", 'r')

    reader = csv.reader(file)

    xValues = []
    yValues = []

    next(reader)

    for row in reader:
        xValues.append(row[0])
        yValues.append(row[1])

    plt.plot(xValues, yValues, 'bo')
    plt.xlabel('Altura')
    plt.ylabel('Latitud')
    plt.title('Latitud en funcion de la altura')
    # plt.axis([-1000, 51000, 33, 85])
    plt.show()
    print("finished")

if __name__ == '__main__':
    printGraph()
