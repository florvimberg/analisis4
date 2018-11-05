class rungeKutta:
    def rungeKutta(self, fun, y0, h, init, end):
        t0 = init
        return self.rungeKuttaPrivado(fun, y0, t0, h, end)

    def rungeKuttaPrivado(self, fun, y, t, h, end):
        k1 = 0
        k2 = 0
        k3 = 0
        k4 = 0

        while t < end:
            k1 = fun(t, y)
            k2 = fun(t + h / 2, y + (h / 2) * k1)
            k3 = fun(t + h / 2, y + (h / 2) * k2)
            k4 = fun(t + h, y + h * k3)
            yNueva = y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
            tNueva = t + h
            return self.rungeKuttaPrivado(fun, yNueva, tNueva, h, end)
        if t >= end:
            return y


if __name__ == '__main__':
    rungeKutta = rungeKutta()

    def func(t, y):
        return 2 * t * y + t

    print(rungeKutta.rungeKutta(func, 0.5, 1, 0, 2))

    print(rungeKutta.rungeKutta(func, 0.5, 0.1, 0, 2))
