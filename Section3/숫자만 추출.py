N=str(input())

def divisor_num(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+=1
    return count
num=[]
for i in range(len(N)):
    if N[i]>='0' and N[i]<='9':
        num.append(N[i])

count=0
res=0
for i in range(len(num)):
    res+=int(num[i])*(10**(len(num)-i-1))
print(res)
print(divisor_num(res))