import matplotlib.pyplot as plt
import csv


def printGraphALAT():
    file = open("files/positions.csv", 'r')

    reader = csv.reader(file)

    xValues = []
    yValues = []

    next(reader)

    for row in reader:
        xValues.append(row[0])
        yValues.append(row[1])

    plt.figure(num=1, figsize=(250, 100))
    for x, y in zip(reversed(xValues), reversed(yValues)):
        plt.plot(x, y, 'co')
    plt.xlabel('Altura')
    plt.ylabel('Latitud')
    plt.title('Latitud en funcion de la altura')
    # plt.axis([-1000, 51000, 33, 85])
    plt.show()
    print("finished")


def printGraphALON():
    file = open("files/positions.csv", 'r')

    reader = csv.reader(file)

    xValues = []
    yValues = []

    next(reader)

    for row in reader:
        xValues.append(row[0])
        yValues.append(row[2])

    plt.figure(num=1, figsize=(250, 100))
    for x, y in zip(reversed(xValues), reversed(yValues)):
        plt.plot(x, y, 'co')
    plt.xlabel('Altura')
    plt.ylabel('Longitud')
    plt.title('Longitud en funcion de la altura')
    # plt.axis([-1000, 51000, 33, 85])
    plt.show()
    print("finished")


if __name__ == '__main__':
    printGraphALAT()
    printGraphALON()
