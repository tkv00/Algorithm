import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 7/7. 송아지 찾기/in1.txt")


from collections import deque
MAX=10000
a,b=map(int,input().split())
dis=[0]*(MAX+1)
ch=[0]*(MAX+1)
dQ=deque()
dQ.append(a)
ch[a]=1
dis[a]=0
while dQ:
    now=dQ.popleft()
    if now==b:
        
        break
    
    for next in (now+1,now-1,now+5):
        if 0<=next<=MAX:
            if ch[next]==0:
                dQ.append(next)
                ch[next]=1
                dis[next]=dis[now]+1
print(dis[b])
