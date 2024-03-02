T=int(input())
res=[]
for _ in range(T):
    test=[]
    N=int(input())
    for i in range(N):
        a,b=map(int,input().split())
        test.append((a,b))
    test.sort(key=lambda x:x[0])
    selected_num=1
    max=test[0][1]
    for i in range(1,N):
        selected_people=test[i][1]
        if selected_people<max:
            max=selected_people
            selected_num+=1
    res.append(selected_num)

for x in res:
    print(x)
    