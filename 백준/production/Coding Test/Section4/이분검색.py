import sys
sys.stdin=open("/Users/kimdoyeon/Downloads/pythonalgorithm_formac/섹션 4/1. 이분검색/in5.txt","rt")

def binary_search(x,start,end,find):
    
    while start<=end:
        mid=(start+end)//2
        if a[mid]==find:
            return mid+1
        elif x[mid]>find:
            end=mid-1
        else:
            start=mid+1
        

N,M=map(int,input().split())
a=list(map(int,input().split()))

a.sort()
mid=len(a)//2
num=binary_search(a,0,len(a)-1,M)
print(num)
