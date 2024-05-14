num,N=map(int,input().split())
num=list(map(int,str(num)))
stack=[]
for x in num:
    while stack and N>0 and stack[-1]<x:
        stack.pop()
        N-=1
    stack.append(x)
if N!=0:
    stack=stack[:-N]
res=''.join(map(str,stack))
print(res)


