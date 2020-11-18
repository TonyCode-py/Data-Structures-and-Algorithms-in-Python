import numpy as np

n = 4
W = 5
Weights = np.array([0,2,1,3,2])
Values = np.array([0,12, 10, 20,15])
F = -np.ones((n+1,W+1))
F[0,:] = 0
F[:,0] = 0

def backpack_dp(i, j):
    if F[i,j] < 0:
        if j < Weights[i]:
            F[i,j] = backpack_dp(i-1, j)
        else:
            F[i,j] = max(backpack_dp(i-1, j),
                         Values[i] + backpack_dp(i-1, j-Weights[i]))

    return F[i,j]
    
print(backpack_dp(n, W))
