import numpy as np

def getCoefficients(x, y):
    """x : array of data points
       y : array of f(x)  """
    x.astype(float)
    y.astype(float)
    n = len(x)
    coefficients = [y[0]]

    for k in range(1, n):
        q = 1
        for j in range(0,k):
            q *= (x[k] - x[j])

        s = 0
        for i in range(0, k):
            aux = 1
            for j in range(0, i):
                aux *= (x[k] - x[j])
            s += (coefficients[i] * aux)

        coefficients.append((y[k] - s)/q)

    return np.array(coefficients)  # return an array of coefficient


def evaluate(a, x, r):
    # ''' a : array returned by function coef()
    #    x : array of data points
    #    r : the node to interpolate at  '''

    x.astype(float)
    n = len(a)
    result = 0

    for i in range(0,n):
        temp = 1
        for j in range(0,i):
            temp *= (r - x[j])

        result += (temp * a[i])

    return result  # return the y_value interpolation

if __name__ == '__main__':
    c = getCoefficients(np.array([1,2,3,4,5,6]), np.array([1,4,9,16,25,36]))
    print(c)
    print (evaluate(c,np.array([1,2,3,4,5,6]),12 ))
