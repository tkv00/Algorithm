import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 6/6. 중복순열 구하기/in1.txt")
def DFS(v):
    global cnt
    if m==v:
        for j in range(m):
            print(res[j],end=' ')
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            res[v]=i
            DFS(v+1) 
if __name__=="__main__":
    n,m=map(int,input().split())
    res=[0]*m
    cnt=0
        