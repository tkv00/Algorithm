import sys

N=int(input())
a=list(map(int,input().split()))
M=int(input())
lt=0
rt=max(a)
while lt<=rt:
    
    sum=0
    mid=(lt+rt)//2
    for i in range(len(a)):
        sum+=min(mid,a[i])
    if sum>M:
        rt=mid-1
    else:
        lt=mid+1
print(rt)
