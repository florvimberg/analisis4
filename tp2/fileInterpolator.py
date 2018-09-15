import csv
import numpy as np
from tp2.newtonInterpolation import getCoefficients
from tp2.newtonInterpolation import evaluate

def csvCreator():

    file = open("files/positions.csv", 'r')

    reader = csv.reader(file)

    w, h = 10, 5000
    # Matrix = [[0 for x in range(w)] for y in range(h)]

    heights = []
    latitudes = []
    longitudes = []

    count = 0
    # count va a ir de 0 a 500, por lo cual vamos a tener 10 sub arreglos
    for row in reader:
        if count <= 50:
            heights.append(float(row[0]))
            latitudes.append(float(row[1]))
            longitudes.append(float(row[2]))

            count += 1

    coefficientsLat = getCoefficients(np.array(heights), np.array(latitudes))
    coefficientsLong = getCoefficients(np.array(heights), np.array(longitudes))

    file = open("files/interpolation.csv", 'w')

    file.write("Altura, Latitud, Longitud \n")

    for i in range(50000, 45000, -1):
        file.write(str(i) + ",")
        file.write(str(evaluate(np.array(coefficientsLat), np.array(heights), i)) + ",")
        file.write(str(evaluate(np.array(coefficientsLong), np.array(heights), i)) + "\n")

if __name__ == '__main__':
    csvCreator()