from sys import stdin
n,m=map(int,stdin.readline().split())
linked=[list(map(int,stdin.readline().split())) for _ in range(n-1)]
question=[list(map(int,stdin.readline().split())) for _ in range(m)]
print(linked)
print(question)