import sys
sys.stdin=open("/Users/kimdoyeon/Downloads/pythonalgorithm_formac/섹션 3/5. 수들의 합/in3.txt","rt")

n,m=map(int,input().split())
a=list(map(int,input().split()))


cnt=p1=0
p2=1
cnt2=0
for num in a:
    if num==m:
        cnt2+=1

while (p1<len(a)):
    if p2<=len(a) and sum(a[p1:p2])==m:
        cnt+=1
        p1+=1
        p2=p1+1
    else:
        if p2<len(a):
            p2+=1
        else:
            p1+=1
            p2=p1+1
            

print(cnt+cnt2)