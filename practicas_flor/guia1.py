import math

from pip._vendor.distlib.compat import raw_input

class guia1:
    def getDerivateSin(self):
        x0 = float("0")
        print("Aproximation of sen function with x = " + str(x0))
        for i in [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]:
            num = (math.sin(x0 + i) - math.sin(x0))
            result = num / float(i)
            print(str(result))

    def getDerivateCos(self):
        for j in [1, 0.5, 0.1, 0.05, 0.01, 0]:
            print("Aproximation of cos function with x = " + str(j))
            for i in [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]:
                num = (math.cos(j + i) - math.cos(j))
                result = num / float(i)
                print(str(result))

    def getDerivatePow(self):
        for j in [1, 0.5, 0.1, 0.05, 0.01, 0]:
            print("Aproximation of x^2 function with x = " + str(j))
            for i in [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]:
                num = (math.pow(j + i,2) - math.pow(j,2))
                result = num / float(i)
                print(str(result))

    # def sum(self):
    #     x = [2.718281828, -3.141592654, 1.414213562, 0.5772156649, 0.3010299957]
    #     y = [1486.2497, 878366.9879, -22.37492, 4773714.647, 0.000185049]
    #     num1 = 0
    #     for i in range(0,5):
    #         num1 += x[i] + y[i]
    #     print("First sum: " + str(num1))
    #
    #     num2 = 0
    #     for i in range(4,-1,-1):
    #         num2 += x[i] + y[i]
    #     print("Second sum: " + str(num2))
    #
    # def sumArranged(self):
    #     x1 = [2.718281828, 1.414213562, 0.5772156649, 0.3010299957]
    #     x2 = [-3.141592654]
    #     y1 = [878366.9879, 4773714.647, 1486.2497, 0.000185049]
    #     y2 = [-22.37492]
    #     num1 = 0
    #     num2 = 0
    #     for i in range(0, 4):
    #         num1 += x1[i] + y1[i]
    #     for j in range(0, 1):
    #         num2 += x2[j] + y2[j]
    #     num3 = num1 + num2
    #     print("Third sum: " + str(num3))

    def evaluateF(self):
        x = [0.125, 0.015625, 1/float(512), 1/float(4096)]
        for i in x:
            f = math.sqrt(math.pow(i, 2) + 1) - 1
            print(f)

    def evaluateG(self):
        x = [0.125, 0.015625, 1 / float(512), 1 / float(4096)]
        for i in x:
            g = math.pow(i, 2) / float(math.sqrt(math.pow(i,2) + 1) + 1)
            print(g)

    def exercise5(self):
        def frange(start, end, step):
            tmp = start
            while (tmp < end):
                yield tmp
                tmp += step

        nums = frange(0.99,1.0002, 0.00001)
        for x in nums:
            f = math.pow(x, 8) - 8 * math.pow(x, 7) + 28 * math.pow(x, 6) - 56 * math.pow(x, 5) + 70 * math.pow(x, 4) - 56 * math.pow(x, 3) + 28 * math.pow(x, 2) - 8 * x + 1
            g = (((((((x - 8) * x + 28) * x - 56) * x + 70) * x - 56) * x + 28) * x - 8) * x + 1
            h = math.pow(x-1, 8)
        print(f)
        print(g)
        print(h)

if __name__ == '__main__':
    guia1 = guia1()
    guia1.exercise5()
