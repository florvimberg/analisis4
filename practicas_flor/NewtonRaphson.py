import math


class NewtonRaphson:

    def getRoot(self, f, a, b):
        if self.sign(f(a)) == self.sign(f(b)):
            return 0
        else:
            c = (a + b) / 2
            if abs(f(c)) < 0.0001:
                return c
            elif self.sign(f(c)) == self.sign(f(a)):
                return self.getRoot(f, c, b)
            elif self.sign(f(c)) == self.sign(f(b)):
                return self.getRoot(f, a, c)

    def sign(self, num):
        if num < 0:
            return -1
        elif num == 0:
            return 0
        else:
            return 1


if __name__ == '__main__':
    newtonRap = NewtonRaphson()


    def func(num):
        return math.pow(num, 3) - 2 * math.pow(num, 2) - 5


    print(newtonRap.getRoot(func, 1, 4))


    def a(x, y):
        print(x, y)


    def b(other, function, args, kwargs):
        function(args, kwargs)
        print(other)


    b('world', a, 'hello', 'dude')
