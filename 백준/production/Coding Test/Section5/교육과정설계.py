import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 5/7. 교육과정 설계/in1.txt")

from collections import deque
str=input()
n=int(input())
queue=[]
queue=deque(str)
print(queue)

p=0

str2=[]
for _ in range(n):
    str2.append(input())

for i in range(n):
    k=str2[i]
    p=0
    num=len(k)
    for j in range(len(k)):
        if k[j]==queue[p]:
            num-=1
            p+=1
    if num==len(k)-len(str):
        print("Y")
    else:
        print("N")
        