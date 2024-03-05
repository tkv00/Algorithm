N,M=map(int,input().split())
a=list(map(int,input().split()))
start=0
end=0
res=0 #최대길이
num=[0]*100001
while end<N:
    if num[a[end]]<M:
        num[a[end]]+=1
        end+=1
    else:
        num[a[start]]-=1
        start+=1
    res=max(res,end-start)
print(res)