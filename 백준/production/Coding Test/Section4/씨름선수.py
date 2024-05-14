import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 4/6. 씨름선수/in5.txt","rt")


N=int(input())
k=[list(map(int,input().split())) for _ in range(N)]


cnt=[0]*N
for i in range(N):
    
    for j in range(i+1,N+i):
        j=j%N
        if k[i][0]>k[j][0] or k[i][1]>k[j][1]:
            cnt[i]+=0
        else:
            cnt[i]+=1
            
count=0
for n in cnt:
    if n==0:
        count+=1

print(count)
        
        
            

