import numpy as np


def getCoefficients(x, y):
    """x : array of data points
       y : array of f(x)  """
    x.astype(float)
    y.astype(float)
    n = len(x)
    coefficients = []

    for i in range(n):
        coefficients.append(0)

    for k in range(0, n, 1):
        coefficients[k] = y[k]

        s = 0.0
        for i in range(0, k, 1):
            multiplication = 1.0
            for j in range(0, i, 1):
                multiplication *= (x[k] - x[j])

            s += multiplication * coefficients[i]

        coefficients[k] -= s

        q = 1.0
        for j in range(0, k, 1):
            q *= (x[k] - x[j])

        coefficients[k] /= q

    return np.array(coefficients)  # return an array of coefficient


def evaluate(a, x, r):
    # ''' a : array returned by function coef()
    #    x : array of data points
    #    r : the node to interpolate at  '''

    x.astype(float)
    n = len(a)
    temp = a[0]
    for i in range(1, n, 1):
        multiplication = a[i]
        for j in range(0, i, 1):
            multiplication *= (r - x[j])

        temp += multiplication

    return temp  # return the y_value interpolation


# if __name__ == '__main__':
#     print(getCoefficients(np.arange(0, 5, 1), np.arange(35, 40, 1)))
#     print(evaluate(getCoefficients(np.arange(0, 5, 1), np.arange(35, 40, 1)), np.arange(0, 5, 1), 2.5))