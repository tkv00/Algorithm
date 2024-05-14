import sys
def DFS(len):
    # if dp[len]>0:
    #     return dp[len]
    if len==1 or len==2:
        return len
    else:
        dp[len]=DFS(len-1)+DFS(len-2)
        return dp[len]
    
if __name__=="__main__":
    n=int(sys.stdin.readline())
    dp=[0]*(n+1)
    print(DFS(n))