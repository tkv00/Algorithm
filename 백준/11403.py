n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]


for mid in range(n):
    for start in range(n):
        for end in range(n):
            if a[start][mid]==1 and a[mid][end]==1:
                a[start][end]=1
for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()
