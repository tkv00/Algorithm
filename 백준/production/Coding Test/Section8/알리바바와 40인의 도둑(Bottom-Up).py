import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 8/7, 8. 알리바바와 40인의 도둑/in5.txt")

n=int(input())
map_list=[list(map(int,input().split())) for _ in range(n)]

dp=[[0]*n for _ in range(n)]
dp[0][0]=map_list[0][0]
for i in range(n):
    for j in range(n):
        #위에서 오는 경우
        if i==0:
            dp[i][j]=dp[0][j-1]+map_list[i][j]
        elif j==0:
            dp[i][j]=dp[i-1][0]+map_list[i][j]
        else:
            dp[i][j]=min(dp[i-1][j],dp[i][j-1])+map_list[i][j]

print(dp[n-1][n-1])