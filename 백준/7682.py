a=[]
res=[]
while True:
    line=input()
    a.append(line)
    if line=="end":
        break
res=[0]*(len(a)-1)
for i in range(len(a)-1):
    if line[i][0]=='O':
        res[i]="invalid"
    else:
        if 