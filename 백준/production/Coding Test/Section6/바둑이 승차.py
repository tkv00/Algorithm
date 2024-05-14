import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 6/5. 바둑이 승차/in5.txt")


def DFS(L,sum):
    global max
    if sum>n:
        return 
    if L==m:
        if sum>max:
            max=sum
        
    else:
        DFS(L+1,sum+a[L])
        DFS(L+1,sum)
        
            

if __name__=="__main__":
    n,m=map(int,input().split())
    max=0
    res=[]
    a=[]
    for i in range(m):
        a.append(int(input()))
    DFS(0,0)
    print(max)