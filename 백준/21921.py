import sys
N,X=map(int,input().split())
a=list(map(int,input().split()))
term=N-X+1
cnt=0

sum=0
dp=[0]*term

for i in range(X):
    sum+=a[i]
dp[0]=sum
max_num=dp[0]
if max(a)==0:
    print("SAD")
    sys.exit(0)

for i in range(1,term):
    dp[i]=dp[i-1]+a[X+i-1]-a[i-1]
    max_num=max(dp[i],max_num)

print(max_num)
for i in range(len(dp)):
    if max_num==dp[i]:
        cnt+=1
print(cnt)
