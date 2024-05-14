import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 4/9. 증가수열 만들기/in2.txt","rt")

n=int(input())
num=list(map(int,input().split()))
lt=0
rt=n-1
tmp=[]
res=""
last=0

while lt<=rt:
    if last<num[lt]:
        tmp.append((num[lt],'L'))
    elif last<num[rt]:
        tmp.append((num[rt],'R'))
    tmp.sort()
    if len(tmp)==0:
        break
    else:
        res+=tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1]=='L':
            lt+=1
        else:
            rt-=1
    tmp.clear()
print(res)
print(len(res))
    