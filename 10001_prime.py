def prime(n):
    count=0
    prime=1
    while count < n:
        prime += 1
        if isprime(prime) == True:
            count += 1
    return prime

def isprime(n):
    if n<2:
        print("neither prime nor composite")        
    else:
        for i in range(2,int(n*0.5)+1):
            if n%i==0:
                return False
        return True

print(prime(10001))
            
            
        
        
        
