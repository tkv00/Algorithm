# 리스트의 값 중 0이 있는지 확인함수
def isZero(a):
    for num in a:
        if num==0:
            return 1

n,k,a,b=map(int,input().split())
plant=[k]*n
day=0
t=0
while True:
    if isZero(plant)==1:
        print(day)
        break
    for i in range(t,t+a):
        plant[i]+=b

    for j in range(n):
        plant[j]-=1

    t=(t+a)%n
    day+=1

