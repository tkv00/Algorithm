import sys
def TreeSum(a,k):
    sum=0
    for i in range(len(a)):
        if a[i]>k:
            sum+=a[i]-k
    return sum

def isBinary(a,N):
    global result
    start=0
    end=max(a)
    while start<=end:
        mid=(start+end)//2
        sum_Tree=0
        sum_Tree=sum(i-mid if i>mid else 0 for i in a)
        if sum_Tree>=N:
            result=mid
            start=mid+1
        else :
            end=mid-1
    return result

result=0
n,m=map(int,sys.stdin.readline().split())
a=list(map(int,sys.stdin.readline().split()))
print(isBinary(a,m))