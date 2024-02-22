import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 8/6. 가장 높은 탑 쌓기(LIS 응용)/in2.txt")

n=int(input())
data=[]
for i in range(1,n+1):
    area,height,weight=map(int,input().split())
    data.append((area,height,weight))
dp=[0]*n
sorted_data=sorted(data,key=lambda x:x[0],reverse=True)
dp[0]=sorted_data[0][1]
for i in range(n):
    max_h=0
    for j in range(i-1,-1,-1):
       
        if sorted_data[i][2]<sorted_data[j][2] and dp[j]>max_h:
            max_h=dp[j]
    dp[i]=max_h+sorted_data[i][1]
print(max(dp))