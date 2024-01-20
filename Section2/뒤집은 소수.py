import math

def reverse(x):
    res=str(x)
    return int(res[::-1])

def is_Prime(x):
    if x==1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

N=int(input())
a=[]
a=list(map(int,input().split()))

for i in range(len(a)):
    num=reverse(a[i])
    if is_Prime(num):
        print(num,end=' ')
