def min(num):
    min=100
    for i in range(len(num)):
        num.append(abs(num[i]-avg))
        if(min>num[i]):
            min=num[i]
    return  min

N=int(input())
num=list(map(int,input().split()))
sum=0
for j in range(len(num)):
    sum+=num[j]
avg=round(sum/N)

for i in range (len(num)):
    if(min(num)==(num[i]-avg)):
        print("%d %d" %(avg,i+1))
        break
else:
    for j in range(len(num)):
        if(-min(num)==(num[i]-avg)):
            print("%d %d" %(avg,j+1))
            break

