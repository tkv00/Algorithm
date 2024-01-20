def add_each(n):
    sum=0
    while(n>0):
        sum+=n%10
        n//=10  #파이썬에서의 몫 구하기 : //
    return sum

def max_(n):
    max=0
    for i in range(len(n)):
        if(max<n[i]):
            max=n[i]
    return max

N=int(input())
a=[]
a=list(map(int,input().split()))
b=[]
for i  in range(N):
    b.append(add_each(a[i]))
for j in range(N):
    if(max_(b)==b[j]):
        print(a[j])
        break
