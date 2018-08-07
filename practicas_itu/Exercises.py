from pip._vendor.distlib.compat import raw_input

class Exercises:
    def maxNum(self):
        num1 = raw_input("write number 1: ")
        num2 = raw_input("write number 2: ")
        num3 = raw_input("write number 3: ")

        if num1 >= num2 and num1 >= num3:
            print(str(num1))
        elif num2 >= num1 and num2 >= num3:
            print(str(num2))
        elif num3 >= num1 and num3 >= num2:
            print(str(num3))
        else:
            print("Error")

    def prime(self):
        num = raw_input("write number: ")
        number = int(num)
        counter = 0
        for i in range(1, number+1):
            if (number % i) == 0:
                counter += 1
        if counter > 2:
            print("false")
        else:
            print("true")


if __name__ == '__main__':
    practice = Exercises()
    for i in range(1, 6):
        practice.maxNum()
