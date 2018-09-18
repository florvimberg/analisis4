import csv
import numpy as np
from tp2.newtonInterpolation import getCoefficients
from tp2.newtonInterpolation import evaluate


def csvCreator():
    file = open("files/positions.csv", 'r')

    reader = csv.reader(file)

    heights = [[0] * 5 for i in range(100)]
    latitudes = [[0] * 5 for i in range(100)]
    longitudes = [[0] * 5 for i in range(100)]

    count = 0
    # count va a ir de 0 a 500, por lo cual vamos a tener 10 sub arreglos
    for row in reader:
        position = int(count / 5)
        innerPosition = count % 5
        heights[position][innerPosition] = float(row[0])
        latitudes[position][innerPosition] = float(row[1])
        longitudes[position][innerPosition] = float(row[2])
        count += 1

    coefficientsLat = []
    coefficientsLong = []

    for i in range(0, 100, 1):
        coefficientsLat.append(getCoefficients(np.array(heights[i]), np.array(latitudes[i])))
        coefficientsLong.append(getCoefficients(np.array(heights[i]), np.array(longitudes[i])))

    file = open("files/interpolation.csv", 'w')

    file.write("Altura, Latitud, Longitud \n")

    for i in range(50000, -1, -1):
        index = 90 - int(i/5000)

        file.write(str(i) + ",")
        file.write(str(evaluate(np.array(coefficientsLat[index]), np.array(heights[index]), i)) + ",")
        file.write(str(evaluate(np.array(coefficientsLong[index]), np.array(heights[index]), i)) + "\n")

if __name__ == '__main__':
    csvCreator()
    print("finished")
