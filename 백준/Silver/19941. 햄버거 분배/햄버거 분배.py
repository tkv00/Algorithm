n,m=map(int,input().split())
a=list(input())
res=[0]*n
for i in range(n):
    if a[i]=='H':
        res[i]=1
cnt=0
for i in range(n):
    if a[i]=='P':
        for j in range(max(0,i-m),min(i+m+1,n)):
            if res[j]==1:
                res[j]=0
                cnt+=1
                break
print(cnt)



