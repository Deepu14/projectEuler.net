def square_diff(n):
    sum1 = lambda x: (x*(x+1)*((2*x)+1))/6
    #print(sum1(n))
    sum2 = lambda x: pow(x * (x + 1) / 2,  2)
    #print(sum2(n))
    difference = lambda x: sum2(x)-sum1(x)
    return difference(n)
print(square_diff(100))
