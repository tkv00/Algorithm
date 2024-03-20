
n=int(input())
building=list(map(int,input().split()))
mid=[]
res=[]
for _ in range(n):
    if not building:
        res.append(0)
        while mid:
            building.append(mid.pop())
        continue
    k=building.pop()
    
    if not building:
        next = 0  # building이 비었다면, 비교 대상이 없으므로 next에 0을 할당
    else:
        next = building[-1]
    if k<=next:
        res.append(len(building))
        while mid:
            building.append(mid.pop())
    elif k>next:
        mid.append(k)
res.reverse()
print(*res)
