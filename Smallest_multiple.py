def smallest_multiple(n):
    for i in range(11,21):
        if n%i == 0:
            continue
        else:
            return False
    return True
n=2520
while not smallest_multiple(n):
    n = n*2 
print(n)
