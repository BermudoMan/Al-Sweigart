import math

def solution(array_a, array_b):
    n = len(array_a)
    sum = 0
    for i in range(n):
        sqr_difference = (array_a[i] - array_b[i])**2
        sum = sum + sqr_difference 
    MSE = sum / n
    return print(MSE)

array_a = [10, 20, 10, 2]
array_b = [10, 25, 5, -2]

solution(array_a, array_b)