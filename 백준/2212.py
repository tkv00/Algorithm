n=int(input())
m=int(input())
a=list(map(int,input().split()))
b=[]
a.sort()
for i in range(n-1):
    b.append(a[i+1]-a[i])
b.sort()

k=sum(b[:(n-m)])
print(k)