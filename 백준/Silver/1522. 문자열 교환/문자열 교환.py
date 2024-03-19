a=list(input())
numA=a.count('a')
cnt=21470000
a=a+a[:numA-1]
for i in range(len(a)-numA+1):
    cnt=min(a[i:numA+i].count('b'),cnt)
print(cnt)