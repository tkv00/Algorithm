n,m=map(int,input().split())
memo=[]
blog=[]
for _ in range(n):
    memo.append(input())
for _ in range(m):
    blog.append(input().split(','))

print(blog)