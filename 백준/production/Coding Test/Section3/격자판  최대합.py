import sys
sys.stdin=open("/Users/kimdoyeon/Downloads/pythonalgorithm_formac/섹션 3/6. 격자판 최대합/in5.txt","rt")

N=int(input())
num=[]
for i in range(N):
    num.append(list(map(int,input().split())))
def sum_cross1(x):
    sum=0
    for i in range(len(x)):
        sum+=x[i][i]
    return sum
def sum_cross2(x):
    sum=0
    for i in range(len(x)):
        sum+=x[i][len(x)-i-1]
    return sum
def sum_row(x):
    sum=0
    max_value=0
    for i in range(len(x)):
        for j in range(len(x)):
            sum+=x[i][j]
            if sum>max_value:
                max_value=sum
        sum=0
    return max_value
        
def sum_col(x):
    sum=0
    max_value=0
    for i in range(len(x)):
        for j in range(len(x)):
            sum+=x[j][i]
            if sum>max_value:
                max_value=sum
        sum=0
    return max_value
max_value=0
res=[]
n1=sum_col(num)
res.append(n1)
n2=sum_row(num)
res.append(n2)
n3=sum_cross1(num)
res.append(n3)
n4=sum_cross2(num)
res.append(n4)
for n in res:
    if max_value<n:
        max_value=n
print(max_value)

        