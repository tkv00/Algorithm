import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 7/2. 휴가/in5.txt")


def DFS(d,m):
    global money_max
    if d>N+1:
        return
    if d==N+1:
        if money_max<m:
            money_max=m
    else:
        DFS(d+time[d],m+money[d])
        DFS(d+1,m)
    
if __name__=="__main__":
    N=int(input())
    time=[]
    money=[]
    time.append(0)
    money.append(0)
    for _ in range(N):
        a,b=map(int,input().split())
        time.append(a)
        money.append(b)

    money_max=-2174000000
    DFS(1,0)
    print(money_max)