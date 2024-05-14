def DFS(L,sum):
    global cnt
    if sum>money:
        return
    elif sum==money:
        if cnt>L:
            cnt=L
    else:
        for i in range(len(a)):
            DFS(L+1,sum+a[i])



if __name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    money=int(input())
    sum=0
    cnt=0
    DFS(0,0)
    print(cnt)
    