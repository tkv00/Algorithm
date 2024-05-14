import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 7/5. 동전분배하기/in4.txt")
import time
start=time.time()
def DFS(L,a_sum,b_sum,c_sum):
    global min_coin
    if N==L:
        if a_sum!=b_sum and b_sum!=c_sum and a_sum!=c_sum:
            k=max(a_sum,b_sum,c_sum)-min(a_sum,b_sum,c_sum)
            if k<min_coin:
                min_coin=k
            
        
    else:
        DFS(L+1,a_sum+a[L],b_sum,c_sum)
        DFS(L+1,a_sum,b_sum+a[L],c_sum)
        DFS(L+1,a_sum,b_sum,c_sum+a[L])
        



if __name__=="__main__":
    N=int(input())
    a=[]
    for _ in range(N):
        a.append(int(input()))
    
    min_coin=217400000
    DFS(0,0,0,0)
    print(min_coin)
    print("time:",time.time()-start)