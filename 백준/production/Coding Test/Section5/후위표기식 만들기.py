a=list(map(str,input()))
stack=[]
res=""
prior={'*':3,'/':3,'+':2,'-':2,'(':1}
for ch in a:
    if ch.isdigit():
        res+=ch
    elif ch==')':
        while stack and stack[-1]!='(':
            res+=stack.pop()
        stack.pop()
    elif ch=='(':
        stack.append(ch)
    else:
        while stack and prior.get(stack[-1],0)>=prior.get(ch,0):
            res+=stack.pop()
        stack.append(ch) 

while stack:
    res+=stack.pop()
print(res)