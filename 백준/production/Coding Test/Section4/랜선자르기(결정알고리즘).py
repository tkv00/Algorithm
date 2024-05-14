import sys
sys.stdin=open("/Users/kimdoyeon/Downloads/pythonalgorithm_formac/섹션 4/2. 랜선자르기/in5.txt","rt")
def is_binary(a,N):
    start=1
    end=max(a)
    while start<=end:
        mid=(start+end)//2
        sum=0
        for i in range(len(a)):
            sum+=a[i]//mid
        if sum>=N:
            result=mid
            start=mid+1
        else:
            end=mid-1
    return result

K,N=map(int,input().split())
a=[]
for i in range(K):
    a.append(int(input()))
n=is_binary(a,N)
print(n)

