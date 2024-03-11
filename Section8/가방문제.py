# import sys
# sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 8/9. 가방문제/in5.txt")

if __name__=="__main__":
    num,weight=map(int,input().split())
    a=[]
    for i in range(num):
        c,b=map(int,input().split())
        a.append((c,b))
    dp=[0]*(weight+1)
    for i in range(num):
        for j in range(a[i][0],weight+1):
            w=a[i][0]
            dp[j]=max(dp[j-w]+a[i][1],dp[j])
print(dp[weight])