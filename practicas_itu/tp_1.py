import math

from pip._vendor.distlib.compat import raw_input
from decimal import *


class Tp1:
    def eMath(self):
        print("The e value from math is: " + str(math.e))

    def eFloat(self):
        number = raw_input("enter number to calculate: ")
        num = float(number)
        res = (1+(1/num)) ** num
        print(res)

    def eDec(self):
        number = raw_input("enter number to calculate: ")
        num = Decimal(number)
        res = (1 + (1 / num)) ** num
        print(res)


if __name__ == "__main__":
    tp1 = Tp1()
    print(tp1.eMath())
    print(tp1.eFloat())
    print(tp1.eDec())
