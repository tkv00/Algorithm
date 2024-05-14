import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 4/8. 침몰하는 타이타닉/in5.txt","rt")

N, M=map(int,input().split())
people=list(map(int,input().split()))

people.sort()
for i in range(1,N):
    if (people[0]+people[i])<=M:
        tmp=i
cnt=0
res=0
for j in range(tmp//2):
    if(people[j]+people[tmp-j])<=M:
        cnt+=1

        
        

print(cnt+tmp+1-(cnt*2)+N-tmp-2)