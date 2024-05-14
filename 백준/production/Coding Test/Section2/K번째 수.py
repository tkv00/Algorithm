def result(N,s,e,k):
    list=[]
    list2=[]
    for i in range(1,N+1):
       list.append(map(int,input().split))
    for i in range(s,e+1):
        list2.append(list[i])
    list2.sort
    print("#",i+1," ",list2[k-1])

T=map(int(input()).split(),end=' ')
for i in range(0,T):
    N,s,e,k=map(int(input()).split())
    result(N,s,e,k)



