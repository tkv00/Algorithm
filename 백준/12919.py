from sys import stdin
import sys
def DFS(s):
    global res
    if s==S:
        print(1)
        sys.exit()
    if len(s)==0:
        return 0
    if s[-1]=='A':
        DFS(s[:-1])
    if s[0]=='B':
        s=s[1:]
        DFS(s[::-1])

if __name__=="__main__":
    res=0
    S=stdin.readline().rstrip()
    T=stdin.readline().rstrip()
    DFS(T)
    print(0)

