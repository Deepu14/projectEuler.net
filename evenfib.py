def even_fib():
    a=0
    b=1
    c=0
    even=[]
    while a+b<=4000000: 
        c=b+a
        if c%2 == 0:
           even.append(c) 
        a=b
        b=c
        print(c)
    print(sum(even))

even_fib()
