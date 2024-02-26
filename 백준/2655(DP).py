
import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 8/6. 가장 높은 탑 쌓기(LIS 응용)/in1.txt")
# 가장높은 탑 쌓기
n=int(input())
top_list=[]
for i in range(n):
    a,b,c=map(int,input().split())
    top_list.append((a,b,c,i+1))
top_list.sort(reverse=True)
dp=[0]*n
dp[0]=top_list[0][1]

for i in range(1,n):
    max_h=0
    for j in range(i):
        if top_list[i][2]<top_list[j][2] and max_h<dp[j]:
            max_h=dp[j]
    dp[i]=max_h+top_list[i][1]

res=max(dp)
index=n-1
history=[]

while index!=-1:
    if dp[index]==res:
        history.append(top_list[index][3])
        res-=top_list[index][1]
    index-=1
print(len(history))
for num in history:
    print(num)
