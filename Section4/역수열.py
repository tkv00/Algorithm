# import sys
# sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 4/10. 역수열/in3.txt","rt")

n=int(input())
num=list(map(int,input().split()))
tmp=[]
res=[]
for i in range(n):
    tmp.append((i+1,num[i]))
tmp.sort(reverse=True)
for i in range(n):
    res.insert(tmp[i][1],tmp[i][0])
print(*res)

