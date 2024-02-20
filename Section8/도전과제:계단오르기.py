import sys
def DFS(k):
    if dp[k]>0:
        return dp[k]
    if k==1 or k==2:
        return dp[k]
    else:
        dp[k]=DFS(k-1)+DFS(k-2)
        return dp[k]
if __name__=="__main__":
    N=int(sys.stdin.readline())
    dp=[0]*(N+1)
    dp[1],dp[2]=1,2
    print(DFS(N))