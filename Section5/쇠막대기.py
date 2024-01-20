import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 5/2. 쇠막대기/in2.txt")
a=list(map(str,input()))
cnt=0
stack=[]
for i in range(len(a)):
    if a[i]=='(':
        stack.append(a[i])
    elif a[i]==')':
        if a[i-1]==')':
            stack.pop()
            cnt+=1
        elif a[i-1]=='(':
            stack.pop()
            cnt+=len(stack)
print(cnt)