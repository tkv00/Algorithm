import sys
sys.stdin=open("/Users/kimdoyeon/Downloads/pythonalgorithm_formac/섹션 3/4. 두 리스트 합치기/in2.txt","rt")

n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int,input().split()))

c=[]
c=a+b
c.sort()
for i in range(len(c)):
    print(c[i],end=' ')


