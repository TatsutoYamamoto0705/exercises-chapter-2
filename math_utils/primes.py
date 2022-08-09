import numpy as np

def isprime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(np.floor(np.sqrt(n))+1)):
            if n%i == 0:
                return False
        return True
            

