import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 6/10. 조합 구하기/in5.txt")

def DFS(L,s):
    global cnt
    
    if L==m:
        for num in res:
            print(num,end=' ')
        print()
        cnt+=1
    else:
        for i in range(s,n+1):
            res[L]=i
            DFS(L+1,i+1)

if __name__=="__main__":
    n,m=map(int,input().split())
    ch=[0]*(n+1)
    res=[0]*m
    cnt=0
    DFS(0)
    print(cnt)