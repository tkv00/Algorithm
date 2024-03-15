n,m=map(int,input().split())
a=[]
for _ in range(n):
    a.append(int(input()))
a.sort(reverse=True)
sum=0
while m>0:
    for num in a:
        k=m//num
        sum+=k
        m=m-(k*num)
print(sum)

    