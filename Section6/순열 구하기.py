import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 6/10. 조합 구하기/in1.txt")

def DFS(L):
    global cnt
    if L==m:
        for i in range(m):
            print(res[i],end=' ')
        print()
        cnt+=1
    else:
        for k in range(1,n+1):
            if ch[k]==0:
                ch[k]=1
                res[L]=k
                DFS(L+1)
                ch[k]=0

if __name__=="__main__":
    n,m=map(int,input().split())
    cnt=0
    res=[0]*m
    ch=[0]*(n+1)
    DFS(0)
    print(cnt)