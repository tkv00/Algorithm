from sys import stdin
import sys

def DFS(L):
    global cnt
    if 
    
    else:
        for _ in range(1,27):
            if (num[L]*10)+num[L]>=1 and (num[L]*10)+num[L]<=26:
                res[L]=(num[L]*10+num[L+1])
                DFS(L+1)
            elif num[L]>=1 and num[L]<=9:
                res[L]=num[L]
                DFS(L+1)

if __name__=="__main__":
    num=list(map(int,input()))
    cnt=0
    res=[0]*(len(num)+1)

    DFS(0,0)
