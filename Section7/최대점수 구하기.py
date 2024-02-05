import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 7/1. 최대점수 구하기/in5.txt")

def DFS(L,time_sum,score_sum,s):
    global max_score
    if time_sum>m:
        return
    if time_sum<=m:
        if score_sum>max_score:
            max_score=score_sum
        for i in range(s,n):
            DFS(L+1,time[i]+time_sum,score_sum+score[i],i+1)

if __name__=="__main__":
    n,m=map(int,input().split())
    time=[0]*n
    score=[0]*n
    for i in range(n):
        score[i],time[i]=map(int,input().split())
    max_score=-217000000
    DFS(0,0,0,0)
    print(max_score)