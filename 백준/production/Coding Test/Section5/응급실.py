import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 5/6. 응급실/in5.txt")
n,m=map(int,input().split())
a=list(map(int,input().split()))
num=[]
ord=[]
for i in range(n):
    num.append(i)
while a:
    if a[0]<max(a):
        a.append(a.pop(0))
        num.append(num.pop(0))
    else:
        a.pop(0)
        ord.append(num.pop(0))
for i in range(len(ord)):
    if m==ord[i]:
        print(i+1)
        break
    