##1. 2차원 리스트로 받기
##2. 각 행별로 중복된 수 찾기
##3. 중복된 수의 중복횟수 구하기
##4. 2,3바탕으로 상금 계산하기
from collections import Counter
N=int(input())
def max_(x):
    max=-2147000000
    for prize in x:
        if prize>max:
            max=prize
    return max

def is_count(x):
    x=set(x)
    if len(x)==1:
        return 3
    elif len(x)==2:
        return 2
    else:
        return 1

def frequency(x):
    counter=Counter(x)
    most_common = counter.most_common(1)[0][0]
    return most_common

def money(x):
    if is_count(x)==3:
        return 10000+frequency(x)*1000
    elif is_count(x)==2:
        return 1000+frequency(x)*100
    elif is_count(x)==1:
        return 100*frequency(x)

a=[]
for i in range(N):
    res=list(map(int,input().split())) 
    a.append(money(res))


print(max_(a))


