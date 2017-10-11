"""def prime_fac(n):
    fac_list=[]
    for i in range(2,n+1):
        if n%i == 0:
            print(i)
            if is_prime(i) == True:
                fac_list.append(i)
    return print(max(fac_list))

def is_prime(m):
    count=0
    for i in range(2,m):
        if m%i == 0:
            return False
    return True

prime_fac(600851475143)
#print(is_prime(29))"""


n= 600851475143
i=2
while i*i < n:
    while n%i == 0:
        n=n/i
        #print(n)
    i=i+1
print(n) 
         
     
