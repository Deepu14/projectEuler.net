"""def sum_primes(primes):
    count=0
    for i in range(2,primes):
        if is_prime(i):
            count = count+i
    return count

def is_prime(n):
    factors=0
    if n<2:
        print("neither prime nor composite")
    else:
        for i in range(1,n+1):
            if n%i == 0:
                factors += 1
        if factors == 2:
            return True
        else:
            return False

print(sum_primes(2000001))"""


def sum_primes(primes):
    prime_list=[]
    for i in range(2,primes+1):
        isPrime=True
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                isPrime=False
                break
        if isPrime:
            prime_list.append(i)
    print(sum(prime_list))
sum_primes(2000001)
                    
