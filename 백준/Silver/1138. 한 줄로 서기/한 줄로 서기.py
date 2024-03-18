n=int(input())
a=list(map(int,input().split()))
res=[0]*n
for i in range(n):
    cur=[]
    for j in range(len(res)):
        if res[j]==0:
            cur.append(j)
    res[cur[a[i]]]=i+1
for num in res:
    print(num,end=' ')
        