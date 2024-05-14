import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 5/5. 공주구하기/in5.txt")
n,m=map(int,input().split())
queue=[]
for i in range(n):
    queue.append(i+1)
while len(queue)>1:
    for _ in range(m-1):
        queue.append(queue.pop(0))
    queue.pop(0)
print(*queue)