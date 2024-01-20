import sys
res=[]
n=int(sys.stdin.readline())
def Change(n):
    if n==1:
        print(1,end='')
        return 1
    Change(n//2)
    print(n%2,end='')
Change(n)