from collections import Counter
def modefinder(numbers):
    c = Counter(numbers)
    order = c.most_common()
    maximum = order[0][1]

    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
    return modes

n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))
res=[]
res.append(sum(a)//n)
a.sort()
res.append(a[n//2])
cnt=[0]*4000
for i in range(n):
    cnt+=1
    cnt.sort()
    if cnt[0]==cnt[1]:
        for
res.append(max(a)-min(a))
for num in res:
    print(num)


