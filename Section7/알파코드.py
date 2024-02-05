from sys import stdin
import sys


def checkNum(arr):
    for num in arr:
        if num<1 or num>26:
            return False
    return True

def DFS(L,s):
    global cnt
    if s>len(num):
        return
    if L==len(num):
        print(res)
    else:
        res[L]=1
        DFS(L+1,s+1)
        res[L]=0
        
        res[L]=2
        DFS(L+1,s+2)
        res[L]=0
        


if __name__=="__main__":
    num=list(map(int,input()))
    cnt=0
    res=[0]*len(num)
    DFS(0,0)
