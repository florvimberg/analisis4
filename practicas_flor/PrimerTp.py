import math

from pip._vendor.distlib.compat import raw_input
from decimal import *


class PrimerTp:
# euler = (1+(1/n))^n
    def mathEuler(self):
        print("This is the euler number given by the math library: " + str(math.e))

    def eulerFloat(self):
        number = raw_input("Enter number to calculate euler number: ")
        num = float(number)
        euler = (1+(1/num)) ** num
        print(euler)

    def eulerDecimal(self):
        number = raw_input("Enter number to calculate euler number: ")
        num = Decimal(number)
        euler = (1+(1/num)) ** num
        print(euler)

    def eulerSpigot(self):
        n = raw_input("Enter amount of digits you want to receive: ")
        euler = "2."
        num = int(n)
        numbers = []
        ones = []
        tens = []
        quotient = [None] * (num)
        suma = [None] * (num)
        resto = [None] * (num)
        for i in range(2,num+2):
            numbers.append(i)
            ones.append(1)
        for i in range(0, num):
            tens.append(ones[i] * 10)
        for i in range(0, num):
            for i in range(num-1, -1,-1):
                if i == num-1:
                    quotient[i] = 0
                    suma[i] = int(tens[i] + quotient[i])
                    resto[i] = int(suma[i] % numbers[i])
                else:
                    quotient[i] = int(suma[i+1]/numbers[i+1])
                    suma[i] = int(tens[i] + quotient[i])
                    resto[i] = int(suma[i] % numbers[i])
            euler += str(int(suma[i] / numbers[i]))
            for i in range(0, num):
                resto[i] *= 10
            tens = resto

        print(euler)


if __name__ == '__main__':
    primerTp = PrimerTp()
    primerTp.mathEuler()
    primerTp.eulerFloat()
    primerTp.eulerDecimal()
    primerTp.eulerSpigot()