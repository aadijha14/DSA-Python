
def max_product(arr):
    # TODO
    max = 0
    for i in range(len(arr)):
        j = i + 1 
        while j < len(arr):
            if arr[i] * arr[j] > max:
                max = arr[i] * arr[j]
            j += 1
    return max


'''
a more efficient solution would be to find the two largest numbers in the array and return their product.
This can be done in a single pass through the array.
'''
def max_product(arr):
    if len(arr) < 2:
        return 0
    max1 = max2 = float('-inf')
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return max1 * max2