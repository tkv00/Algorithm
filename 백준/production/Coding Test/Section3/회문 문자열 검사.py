N=int(input())

def is_string(str):
    str=str.upper()
    if str==str[::-1]:
        return True
    else:
        return False
    
word=[]
for i in range(N):
    word.append(str(input()))

for i in range(len(word)):
    if(is_string(word[i])):
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))