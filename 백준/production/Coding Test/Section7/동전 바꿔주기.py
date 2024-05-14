import sys
from sys import stdin
import time
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 7/4. 동전바꿔주기/in5.txt")
start=time.time()
def DFS(L,sum):
    global cnt
    if sum>T:
        return
    if L==k:
        if sum==T:
            cnt+=1

    else:
        c=count[L]
        for j in range(c+1):
            DFS(L+1,sum+(cost[L]*j))

if __name__=="__main__":
    T=int(stdin.readline())
    k=int(stdin.readline())
    cost=[]
    count=[]
    for _ in range(k):
        a,b=map(int,stdin.readline().split())
        cost.append(a)
        count.append(b)
    cnt=0
    DFS(0,0)
    print(cnt)
    print("time : ",time.time()-start)