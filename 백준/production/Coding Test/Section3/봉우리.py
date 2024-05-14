import sys
sys.stdin=open("/Users/kimdoyeon/Downloads/pythonalgorithm_formac/섹션 3/9. 봉우리/in5.txt","rt")

def find_max(num,N):
    N=N+2
    is_peak=[[0 for _ in range(N)] for _ in range(N)]
    count=0
    for i in range(1,N-1):
        for j in range(1,N-1):
            if num[i][j]>num[i-1][j] and num[i][j]>num[i+1][j] and num[i][j]>num[i][j-1] and num[i][j]>num[i][j+1]  and is_peak[i][j]==0:
                is_peak[i][j]=1
            #리스트 중 맥스를 찾으면 주변값이 같아도 인정되므로
            #해당값 num[i][j]의 값이 주변보다 커야함.(같은 것은 인정 ㄴㄴ)
    for i in range(N):
        for j in range(N):
            if is_peak[i][j]==1:
                count+=1
    return count
    


N=int(input())
numList=[[0 for _ in range(N+2)] for _ in range(N+2)]

a=[list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        numList[i+1][j+1]=a[i][j]

num=find_max(numList,N)
print(num)


