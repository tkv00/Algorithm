import sys
sys.stdin=open("/Users/kimdoyeon/Downloads/pythonalgorithm_formac/섹션 3/8. 곳감/in1.txt","rt")

def is_sum(x,N):
    index=N
    n=index//2
    sum1=0
    for i in range(N):
        if i<index//2 :
            a=b=0
            for i in range(n):
                sum1+=sum(x[n-a-1][n-b-1:n+b+1])
                a+=1
                b+=1
        elif i>=index//2:
            a=b=0
            for i in range(n+1):
                sum1+=sum(x[n+a][n-b:n+b])
                a+=1
                b+=1

    return sum1

N=int(input())
num=[]
for i in range(N):
    num.append(list(map(int,input().split())))

is_sum(num,N)
M=int(input())
ord=[]
for i in range(M):
    ord.append(list(map(int,input().split())))

