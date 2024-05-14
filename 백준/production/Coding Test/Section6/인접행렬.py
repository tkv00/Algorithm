

n,m=map(int,input().split())
a=[[0]*n for _ in range(n) ]
for _ in range(m):
    x,y,money=map(int,input().split())
    a[x-1][y-1]=money
for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()