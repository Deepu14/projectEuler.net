def multiples():
    a=[]
    for i in range(1,1000):
        if i%3==0 or i%5==0:
            a.append(i)
    return sum(a)
            
print(multiples())
