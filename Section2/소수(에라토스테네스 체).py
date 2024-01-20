import math
def is_prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

N=int(input())
a=[]
for i in range(2,N+1):
    if is_prime(i)==True:
        a.append(i)

print(len(a))
