import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 6/11. 수들의 조합/in5.txt")

def DFS(L,sum,s):
    global cnt
    if L==m:
        if sum%k==0:
            cnt+=1 
    else:
        for i in range(s,n):
            DFS(L+1,sum+a[i-1],i+1)

    
if __name__=="__main__":
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    k=int(input())
    res=[0]*m
    cnt=0
    DFS(0,0,0)
    print(cnt)