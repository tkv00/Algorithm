import sys
sys.stdin=open("/Users/kimdoyeon/Downloads/pythonalgorithm_formac/섹션 3/7. 사과나무/in5.txt","rt")

N=int(input())
num=[]
for i in range(N):
    num.append(list(map(int,input().split())))
Matrix_sum=0
s=e=N//2
for i in range(N):
    for j in range(s,e+1):
        Matrix_sum+=num[i][j]
    if i<N//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(Matrix_sum)
        
            
                
        
            
            
    
    