import sys

from utils import elapsed_time


def classic_matrixChainMultiplication(dims, i, j):
 
    if j <= i + 1:
        return 0
 
    min = sys.maxsize
 
    for k in range(i + 1, j):
        cost = classic_matrixChainMultiplication(dims, i, k)
        cost += classic_matrixChainMultiplication(dims, k, j)
        cost += dims[i] * dims[k] * dims[j]
        if cost < min:
            min = cost 
    return min
 

def dyn_matrixChainMultiplication(dims):
 
    n = len(dims)
    c = [[0 for x in range(n + 1)] for y in range((n + 1))]
    for length in range(2, n + 1):        
 
        for i in range(1, n - length + 2):
 
            j = i + length - 1
            c[i][j] = sys.maxsize
 
            k = i
            while j < n and k <= j - 1:
                cost = c[i][k] + c[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
 
                if cost < c[i][j]:
                    c[i][j] = cost
 
                k = k + 1
 
    return c[1][n - 1]

def run_matrix():
    import random
    results_class, result_dyn = [], []
    
    for i in range(10,20):
        dims = [random.randint(10,100) for i in range(i)]
        r = elapsed_time(classic_matrixChainMultiplication, dims, 0, len(dims) - 1, text=f"Matrix chain with n = {i}")
        results_class.append(r)
        r= elapsed_time(dyn_matrixChainMultiplication, dims, text=f"Matrix chain with n = {i}")
  
    return (results_class, result_dyn
        )
