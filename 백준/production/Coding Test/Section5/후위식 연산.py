import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 5/4. 후위식 연산/in5.txt")

a=list(map(str,input()))
stack=[]
for x in a:
    if x.isdigit():
        stack.append(x)
    else:
        op1=int(stack.pop())
        op2=int(stack.pop())
        if x=='+':
            stack.append(op2+op1)
        elif x=='-':
            stack.append(op2-op1)
        elif x=='/':
            stack.append(op2//op1)
        else:
            stack.append(op2*op1)
print(stack.pop())            
