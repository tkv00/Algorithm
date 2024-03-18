
def Man(k,num):
    for i in range(1,len(k)):
        if i%num==0:
            if k[i]==1:
                k[i]=0
            elif k[i]==0:
                k[i]=1

def WoMan(k,num):
    # if k[num]==1:
    #     k[num]=0
    # elif k[num]==0:
    #     k[num]=1
    for i in range(len(k)-1//2):
        if num+i>len(k)-1 or num-i<1: break
        if k[num-i]==k[num+i]:
            if k[num-i]==1:
                k[num-i]=0
                k[num+i]=0
            else:
                k[num-i]=1
                k[num+i]=1
        else: break


if __name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    a.insert(0,-1)
    student_num=int(input())
    std_list=[]
    for _ in range(student_num):
        sex,num=map(int,input().split())
        if sex==1:
            Man(a,num)
        if sex==2:
            WoMan(a,num)
    
    for i in range(1,n+1):
        print(a[i],end=' ')
        if i%20==0:
            print()
    
