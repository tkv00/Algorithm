def binary(k):
    start=0
    end=max(a)
    while start<=end:
        mid=(start+end)//2
        if mid>=k:
            start=mid+1
        else:
            end=mid-1
N=int(input())
a=list(map(int,input().split()))
M=int(input())
b=list(map(int,input().split()))
a.sort()
start=0
end=max(a)
