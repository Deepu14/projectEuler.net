def largest_palindrome():
    n=0
    for i in range(100,1000):
        for j in range(100,1000):
            k=(i*j)
            if k >n:
                k=str(k)
                if k==k[::-1]:
                    n=i*j
    return n
    
print(largest_palindrome())



                
                
