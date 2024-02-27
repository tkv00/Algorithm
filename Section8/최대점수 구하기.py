import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 8/11. 최대점수 구하기(냅색알고리즘)/in1.txt")

def DFS(L,t):
    global sum
    if t>time:
        return 
    else:
        DFS(L+1,t+a[L][1])
        dp[L]=dp[L-1]+a[L][0]
        sum=max(dp[L],sum)
        DFS(L+1,t)
        dp[L]=dp[L-1]


if __name__=="__main__":
    sol,time=map(int,input().split())
    a=[]
    sum=0
    for i in range(sol):
        k,t=map(int,input().split())
        a.append((k,t))
    dp=[0]*(time+1)
    DFS(0,0)
    print(sum)

