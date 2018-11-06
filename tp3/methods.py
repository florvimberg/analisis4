import math
import csv

from numpy import genfromtxt


def logisticCurve(m, k, t):
    return m / (1 + math.e ** (-k * m * t))


def runge_kutta(y, interval, h, t, m, k):
    if t == interval[1]:
        return y

    k1 = calculate(t, y, m, k)
    k2 = calculate(t + (h / 2), y + (h * k1 / 2), m, k)
    k3 = calculate(t + (h / 2), y + (h * k2 / 2), m, k)
    k4 = calculate(t + h, y + (h * k3), m, k)

    newY = y + (h * (k1 + 2 * k2 + 2 * k3 + k4)) / 6
    newT = t + h

    return runge_kutta(newY, interval, h, newT, m, k)


def calculate(_, y, m, k):
    return k * y * (m - y)

def difs():
    for t in range(10):
        results = open("files/results/resultT" + str(t) + ".csv", 'w')

        rkArray = genfromtxt('files/RungeKutta/RungeKuttaT' + str(t) + '.csv', delimiter=',')
        lcArray = genfromtxt('files/logisticCurve/logisticCurveT' + str(t) + '.csv', delimiter=',')

        for i in range(5):
            for j in range(10):
                if j == 9:
                    results.write(str(abs(float(lcArray[i][j]) - float(rkArray[i][j]))))
                else:
                    results.write(str(abs(float(lcArray[i][j]) - float(rkArray[i][j])))) + results.write(", ")
            results.write("\n")


def run():
    file = open("files/coeficientes_canal.csv", 'r')

    reader = csv.reader(file)

    coefs = [0 for _ in range(5)]

    count = 0
    for row in reader:
        val = float(row[0])
        coefs[count] = val
        count += 1

    file = open("files/televidentes_canal_horario.csv", 'r')

    reader = csv.reader(file)

    viewers = [[0] * 10 for _ in range(5)]

    count = 0
    for row in reader:
        for i in range(10):
            val = int(row[i])
            viewers[count][i] = val

        count += 1

    for t in range(0, 10, 1):
        file = open("files/RungeKuttaT" + str(t) + ".csv", 'w')
        for k in range(5):
            for m in range(10):
                if m == 9:
                    file.write(str(
                        runge_kutta(logisticCurve(viewers[k][m], coefs[k], t), [t, t + 1], 0.25, t, viewers[k][m],coefs[k])))
                else:
                    file.write(str(runge_kutta(logisticCurve(viewers[k][m],coefs[k],t), [t, t+1], 0.25, t, viewers[k][m], coefs[k]))) + file.write(", ")
            file.write("\n")


if __name__ == '__main__':
    difs()
