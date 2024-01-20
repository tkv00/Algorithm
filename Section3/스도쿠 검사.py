import sys
sys.stdin=open("/Users/kimdoyeon/Downloads/pythonalgorithm_formac/섹션 3/10. 스도쿠 검사/in5.txt","rt")

myList=[list(map(int,input().split())) for _ in range(9)]

correct=[1,2,3,4,5,6,7,8,9]

#행 비교
res=0
for i in range(9):

    ex_list=myList[i].copy()
    ex_list.sort()
    if ex_list!=correct:
        res+=1
        

for i in myList:
    row=[]
    for j in range(9):
        row.append(i[j])
        row.sort()
    if row!=correct:
        res+=1
            



number=[[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
for a,b in number:
    All=[]
    for j in range(a,3+a):
        for k in range(b,3+b):
            All.append(myList[j][k])
    All.sort()
    if All!=correct:
        res+=1



if res==0:
    print("YES")
else:
    print("NO")