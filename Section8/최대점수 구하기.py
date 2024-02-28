import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 8/11. 최대점수 구하기(냅색알고리즘)/in5.txt")
n,m=map(int,input().split())
a=[]
for i in range(n):
    N,T=map(int,input().split())
    a.append((N,T))
    
dp=[0]*(m+1)
for i in range(n):
    for j in range(m,a[i][1]-1,-1):
        dp[j]=max(dp[j],a[i][0]+dp[j-a[i][1]])
print(dp[m])
