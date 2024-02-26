import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 8/6. 가장 높은 탑 쌓기(LIS 응용)/in5.txt")

n=int(input())
top=[]
for i in range(n):
    a,b,c=map(int,input().split())
    top.append((a,b,c))
top.sort(reverse=True)

dp=[0]*n
dp[0]=top[0][1]
res=0
for i in  range(1,n):
    max=0
    for j in range(i):
        if top[i][2]<top[j][2] and dp[j]>max:
            max=dp[j]
    dp[i]=max+top[i][1]
    if res<dp[i]:
        res=dp[i]
print(res)
