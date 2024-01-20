import heapq
heap=[]
res=[]
while True:
    num=int(input())
    if num==-1:
        break
    elif num==0:
        res.append(heapq.heappop(heap))
    else:
        heapq.heappush(heap,num)

for num in res:
    print(num)