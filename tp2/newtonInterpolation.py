import numpy as np

def getCoefficients(x, y):
    """x : array of data points
       y : array of f(x)  """
    x.astype(float)
    y.astype(float)
    n = len(x)
    result = []
    for i in range(n):
        result.append(y[i])

    for k in range(1, n):

        for i in range(n - 1, k - 1, -1):
            result[i] = float(result[i] - result[i - 1]) / float(x[i] - x[i - k])

    return np.array(result)  # return an array of coefficient


def evaluate(a, x, r):
    # ''' a : array returned by function coef()
    #    x : array of data points
    #    r : the node to interpolate at  '''

    x.astype(float)
    n = len(a) - 1
    temp = a[n]
    for i in range(n - 1, -1, -1):
        temp = temp * (r - x[i]) + a[i]
    return temp  # return the y_value interpolation
