import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 7/2. 휴가/in2.txt")


def DFS(L,m,t):
    global money_sum
    if t>N:
        return
    elif t<=N:
        if m>money_sum:
            money_sum=m
            print(money_sum)
        for i in range(N):
            if ch[i]==0:
                k=money[i]
                ch[:k]==1
                DFS(L+1,m+money[i],t+time[i])
                ch[:k]=0
    
    
if __name__=="__main__":
    N=int(input())
    time=[]
    money=[]
    for _ in range(N):
        a,b=map(int,input().split())
        time.append(a)
        money.append(b)
    ch=[0]*(N+1)
    money_sum=-2174000000
    DFS(0,0,0)
    print(money_sum)