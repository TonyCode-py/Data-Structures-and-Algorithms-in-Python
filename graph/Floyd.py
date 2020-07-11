def Floyd(A, n):
    """A为n*n的矩阵"""
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(A[i,k]+A[k,j] < A[i,j]):
                    A[i,j] = A[i,k]+A[k,j]
    return A
