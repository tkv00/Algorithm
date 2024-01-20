import sys
import heapq
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 5/11. 최대힙/in5.txt")
heap=[]
res=[]
while True:
    num=int(input())
    if num==-1:
        break
    elif num==0:
        res.append(heapq.heappop(heap))
    else:
        heapq.heappush(heap,-num)
for num in res:
    print(-num)