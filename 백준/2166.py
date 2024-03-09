N=int(input())
a=[]
for i in range(N):
    x,y=map(int,input().split())
    a.append((x,y))
res1=0
res2=0
for i in range(N-1):
    res1+=a[i][0]*a[i+1][1]
    res2+=a[i][1]*a[i+1][0]
res1+=a[N-1][0]*a[0][1]
res2+=a[N-1][1]*a[0][0]
area=abs(res1-res2)/2
print(area)
