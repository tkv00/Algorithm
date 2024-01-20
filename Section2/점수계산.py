N=int(input())
a=list(map(int,input().split()))

def sum(x):
    sum=0
    for num in x:
        sum+=num
    return sum

res=[]
count=0
i=0
while i<len(a):
    if a[i]==1:
        res.append(1)
        i+=1
        count=1
        while i<len(a) and a[i]!=0:
            count+=1
            i+=1
            res.append(count)
        count=0
    elif a[i]==0:
        res.append(0)
        i+=1
        
print(sum(res))

