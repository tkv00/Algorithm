
n=int(input())
member=[]
for _ in range(n):
    a,b=input().split()
    a=int(a)
    member.append((a,b))

member.sort(key=lambda x:x[0])
for mem in member:
    print(mem[0],mem[1])
