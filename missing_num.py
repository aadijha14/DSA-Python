
def missing_number(arr, n):
    sum1 = n * (n+ 1)//2
    sum2 = sum(arr)
    miss = sum1 - sum2
    return miss
        
