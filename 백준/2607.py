def isSame(origin,other):
    if origin==other:
        return 1
    elif abs(len(origin)-len(other))<=1:
        #한 문자를 다른 문자로 바꿀 때
        for i in range(len(other)):
            for j in range(len(origin)):
                if other[:i]+other[i+1:]==origin[:j]+origin[j+1:]:
                    return 1
        if len(origin)>len(other):
        #한 문자를 더할 때
            for i in range(len(origin)):
                if origin[:i]+origin[i+1:]==other:
                    return 1
        else:
            
            #한 문자를 뺄 때
            for i in range(len(other)):
                if other[:i]+other[i+1:]==origin:
                    return 1
            
        
    return 0
    
if __name__=="__main__":
    n=int(input())
    a=[]
    for _ in range(n):
        k=list(input())
        k.sort()
        a.append(k)
    
    cnt=0
    for i in range(1,n):
        if isSame(a[0],a[i])==1:
            cnt+=1
    
    print(cnt)