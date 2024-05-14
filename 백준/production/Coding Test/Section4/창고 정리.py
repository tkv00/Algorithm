import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 4/7. 창고 정리/in5.txt","rt")
N=int(input())
box=list(map(int,input().split()))
set_time=int(input())

for i in range(set_time):
    box.sort()
    box[0]+=1
    box[N-1]-=1
box.sort()
res=box[N-1]-box[0]
print(res)