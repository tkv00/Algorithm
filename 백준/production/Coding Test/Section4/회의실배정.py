import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 4/5. 회의실 배정/in5.txt","rt")

N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
a.sort(key=lambda x:x[1])
time=0
cnt=0
for i in range(0,N):
    if time<=a[i][0]:
        cnt+=1
        time=a[i][1]
print(cnt)
    