import sys
import random


def Qsort(lt,rt):
    if lt<rt:
        pivot_index = random.randint(lt, rt)
        arr[rt], arr[pivot_index] = arr[pivot_index], arr[rt] 
        pivot=arr[rt][0]
        pos=lt
        for i in range(lt,rt):
            if pivot>arr[i][0]:
                arr[pos],arr[i]=arr[i],arr[pos]
                pos+=1
            elif pivot==arr[i][0]:
                if arr[rt][1]>arr[i][1]:
                    arr[pos],arr[i]=arr[i],arr[pos]
                    pos+=1
        arr[pos],arr[rt]=arr[rt],arr[pos]
        
        Qsort(lt,pos-1)
        Qsort(pos+1,rt)
    
if __name__=="__main__":
    N=int(sys.stdin.readline().strip())
    arr=[]
    for i in range(N):
        a,b=map(int,sys.stdin.readline().strip().split())
        arr.append((a,b))
    Qsort(0,N-1)
    for i in range(N):
        sys.stdout.write(f"{arr[i][0]} {arr[i][1]}\n")
# 파이썬으로 퀵정렬 할 때 시간초과 나면 pivot값을 랜덤으로 선정