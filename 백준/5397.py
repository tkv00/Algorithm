from collections import deque
def Result(k):
    dq_left = deque()
    dq_right = deque()
    for i in range(len(k)):
        if k[i]=='<':
            if len(dq_left)>0:
                t=dq_left.pop()
                dq_right.appendleft(t)
        if k[i]=='>':
            if len(dq_right)>0:
                t=dq_right.pop()
                dq_left.appendleft(t)
        if k[i]=='-':
            dq_left.pop()
        else:
            dq_left.appendleft(k[i])

if __name__ == '__main__':
    n=int(input())
    a=[]
    res=[]
    for _ in range(n):
        a = list(input())
    for i in range(n):
        res.append(Result(a[i]))
    print(res)


