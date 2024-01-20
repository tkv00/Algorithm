def max(list):
    max=0
    for i in range(len(list)):
        if(max<list[i]):
            max=list[i]
    return max
N, M=map(int,input().split())
a=[]
count=[0]*(N+M+1)
for i in range(N):
    b=[]
    for j in range(M):
        b.append(i+j+2)
        count[i+j+2]+=1
    a.append(b)
    
for j in range(len(count)):
    if(max(count)==count[j]):
        print(j,end=' ')
    
