plate_Num,sushi,complete,coupon=map(int,input().split())
a=[]
for i in range(plate_Num):
    a.append(int(input()))

res=0
cnt=0
for start in range(plate_Num):
    end=(start+complete)
    if end>plate_Num:
        end=end%plate_Num
        tmp=set(a[start:]+a[:end])
    else:
        tmp=set(a[start:end])
    cnt=len(tmp)
    if coupon in tmp:
        cnt+=0
    else: 
        cnt+=1
    res=max(res,cnt)
print(res)
