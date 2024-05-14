import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 5/9. 아나그램(구글)/in5.txt")
def isTrue(p1,p2):
    cnt=0
    if all(val==p2[key] for key,val in p1.items()):
        print("YES")
    else:
        print("NO")

a=list(map(str,input()))
b=list(map(str,input()))
p1=dict()
p2=dict()
for x in a:
    if x in p1:
        p1[x]+=1
    else:
        p1[x]=1
for y in b:
    if y in p2:
        p2[y]+=1
    else:
        p2[y]=1
isTrue(p1,p2)

