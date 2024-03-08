T=int(input())
res=[0]*T
for i in range(T):
    N=int(input())
    a=list(map(int,input().split()))
    sum=0
    max=-1
    for j in range(N-1,-1,-1):
        if max<a[j]:
            max=a[j]
        else:
            res[i]+=max-a[j]
for num in res:
    print(num)