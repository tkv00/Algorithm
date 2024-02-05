import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 6/9. 수열 추측하기/in2.txt")

def DFS(L,sum):

    if L==n and sum==m:
        for k in res:
            print(k,end=' ')
        print()
        sys.exit(0)
    else:
        for j in range(1,n+1):
            if ch[j]==0:
                ch[j]=1
                res[L]=j
                DFS(L+1,sum+b[L]*res[L])
                ch[j]=0




if __name__=="__main__":
    n,m=map(int,input().split())
    res=[0]*n
    b=[1]*(n+1)
    for i in range(1,n):
        b[i]=b[i-1]*(n-i)//i
    ch=[0]*(n+1)
    DFS(0,0)