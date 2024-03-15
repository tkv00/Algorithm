from collections import deque

if __name__=="__main__":
    N,M=map(int,input().split())
    dq=deque()
    dq.append(N)
    res=[0]*100001
    while dq:
        k=dq.popleft()
        if k==M:
            print(res[M])
            break
        for next in (k*2,k-1,k+1):
            if 0<=next<=100000 and res[next]==0:
                if next==k*2:
                    res[next]=res[k]
                else :
                    res[next]=res[k]+1
                dq.append(next)
