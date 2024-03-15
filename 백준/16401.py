m,n=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
start=1
end=max(a)
while start<=end:
    sum=0
    mid=(start+end)//2
    for i in range(n):
        sum+=a[i]//mid
    if sum>=m:
        start=mid+1
    else:
        end=mid-1
print(end)