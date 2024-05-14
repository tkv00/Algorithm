import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 8/5. 최대 선 연결하기/in5.txt")

N=int(input())
a=list(map(int,input().split()))
dp=[0]*(N+1)
a.insert(0,0)
dp[1]=1
num=0
for i in range(2,N+1):
    max=0
    for j in range(i-1,0,-1):
        if a[i]>a[j] and dp[j]>max:
            max=dp[j]
    dp[i]=max+1
    if dp[i]>num:
        num=dp[i]
print(num)
