
N,M=map(int,input().split())
a=[]
for _ in range(N):
    a.append(int(input()))

cnt=0

start=1
end=max(a)

while start<=end:
    mid=(start+end)//2
    count = sum(cable//mid for cable in a)
    if count>=M:
        start=mid+1
        
    else:
        end=mid-1
       

print(end)