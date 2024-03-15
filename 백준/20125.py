N=int(input())
cookie=[[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    line=input()
    for j,char in enumerate(line,start=1):
        cookie[i][j]=char
tmp=[]

for i in range(1,N+1):
    for j in range(1,N+1):
        if cookie[i][j]=='*':
            tmp.append((i,j))

tmp.sort(key=lambda x:x[0])
head_x=tmp[0][0]
head_y=tmp[0][1]
left_hand=0
right_hand=0
for i in range(1,head_y):
    if cookie[head_x+1][i]=='*':
        left_hand+=1
for i in range(head_y+1,N+1):
    if cookie[head_x+1][i]=='*':
        right_hand+=1
body=0
i=0
while True:
    if cookie[head_x+i][head_y]=='_':
        break
    body+=1
    i+=1
left_leg=0
right_leg=0
for i in range(head_x+body,N+1):
    if cookie[i][head_y-1]=='*':
        left_leg+=1
    if cookie[i][head_y+1]=='*':
        right_leg+=1


print(head_x+1,head_y)
print(left_hand,right_hand,body-2,left_leg,right_leg)