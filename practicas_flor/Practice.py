from pip._vendor.distlib.compat import raw_input


class Practice:
    def getHigher(self):
        print("In this exercise you write three numbers and we return the highest one")
        num1 = raw_input("Enter the first number: ")
        num2 = raw_input("Enter the second number: ")
        num3 = raw_input("Enter the third number: ")
        if num1 >= num2 and num1 >= num3:
            print(str(num1))
        elif num2 >= num1 and num2 >= num3:
            print(str(num2))
        elif num3 >= num1 and num3 >= num2:
            print(str(num3))
        else:
            print("algo salio mal")

    def isPrime(self):
        print("In this exercise you write a number a we say if its prime or not")
        num = raw_input("Enter the number: ")
        number = int(num)
        count = 0
        for i in range(1, number+1):
            if (number % i) == 0:
                count += 1
        if count > 2:
            print("False")
        else:
            print("True")


if __name__ == '__main__':
    practice = Practice()
    for i in range(1, 6):
        practice.isPrime()
