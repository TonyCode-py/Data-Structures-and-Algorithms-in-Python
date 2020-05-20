"""
Author: Tony Code
"""

import numpy as np

def linear_regression(X, Y):
    """
    Assume y = a + bx. Calculate a and b from X and Y.
    
    """
    x_ = np.array([(x-np.mean(X)) for x in X])
    y_ = np.array([(y-np.mean(Y)) for y in Y])
    
    Sxx = np.sum(x_ ** 2)
    Sxy = np.sum(x_ * y_)

    b = Sxy / Sxx
    a = np.mean(Y) - np.mean(X) * b

    return a, b

def main():
    #dataset
    X = np.array([100,110,120,130,140,150,160,170,180,190])
    Y = np.array([45,51,54,61,66,70,74,78,85,89])

    #calculate coefficient
    a, b = linear_regression(X, Y)

    print(f'y = {a:.6} + {b:.6}x')

if __name__ == '__main__':
    main()
