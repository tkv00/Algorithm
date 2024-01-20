import sys
sys.stdin=open("/Users/kimdoyeon/Downloads/pythonalgorithm_formac/섹션 3/11. 격자판 회문수/in2.txt","rt")

a=[list(map(int,input().split())) for _ in range(7)]
def is_reverse(x):
    for i in range(len(x)//2):
        if x[i]!=x[-i-1] :
            return False
    
    return True

cnt=0
myList1=[]
res=[]
myList2=[]

for i in range(7):
    for j in range(3):
        if is_reverse(a[i][j:j+5]):
            cnt+=1


for i in range(7):
    for j in range(3):
        myList2=[a[k][i] for k in range(j,j+5)]
        if is_reverse(myList2):
            cnt+=1

print(cnt)
