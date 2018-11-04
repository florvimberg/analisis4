import matplotlib.pyplot as plt
import csv
from mpl_toolkits.mplot3d import Axes3D


def printGraphALAT():
    file = open("files/interpolation.csv", 'r')

    reader = csv.reader(file)

    xValues = []
    yValues = []

    next(reader)

    for row in reader:
        xValues.append(row[0])
        yValues.append(row[1])

    xTemp = []
    yTemp = []
    i = 0
    while i < len(xValues):
        xTemp.append(float(xValues[i]))
        yTemp.append(float(yValues[i]))
        i += 10

    x = list(map(float, reversed(xTemp)))
    y = list(map(float, reversed(yTemp)))
    plt.plot(x, y, 'co')
    plt.xlabel('Altura')
    plt.ylabel('Latitud')
    plt.title('Latitud en funcion de la altura')
    plt.show()
    print("finished")


def printGraphALON():
    file = open("files/interpolation.csv", 'r')

    reader = csv.reader(file)

    xValues = []
    yValues = []

    next(reader)

    for row in reader:
        xValues.append(row[0])
        yValues.append(row[2])

    xTemp = []
    yTemp = []
    i = 0
    while i < len(xValues):
        xTemp.append(float(xValues[i]))
        yTemp.append(float(yValues[i]))
        i += 10

    x = list(map(float, reversed(xTemp)))
    y = list(map(float, reversed(yTemp)))
    plt.plot(x, y, 'co')
    plt.xlabel('Altura')
    plt.ylabel('Longitud')
    plt.title('Longitud en funcion de la altura')
    plt.show()
    print("finished")


def printGraph():
    file = open("files/interpolation.csv", 'r')

    reader = csv.reader(file)
    fig = plt.figure()
    ax = Axes3D(fig)

    xValues = []
    yValues = []
    zValues = []

    next(reader)

    for row in reader:
        xValues.append(row[2])  # longitud
        yValues.append(row[1])  # latitud
        zValues.append(row[0])  # altura

    x = list(map(float, reversed(xValues)))
    y = list(map(float, reversed(yValues)))
    z = list(map(float, reversed(zValues)))
    ax.scatter3D(x, y, z, cmap='Greens')
    ax.set_title('Altura, Latitud, Longitud')
    ax.set_xlabel('longitud')
    ax.set_ylabel('latitud')
    ax.set_zlabel('altura')

    plt.show()
    print("finished")


if __name__ == '__main__':
    printGraph()
