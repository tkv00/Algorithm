def DFS(str,gather_num,consonant_num,index_num):

    if len(str)==n:
        if gather_num>=1 and consonant_num>=2:
            print(''.join(str))
        return
    for i in range(index_num+1,len(a)):
        alpha=a[i]
        if alpha not in str:
            if alpha in 'aeiou':
                DFS(str+alpha,gather_num+1,consonant_num,i)
            else:
                DFS(str+alpha,gather_num,consonant_num+1,i)
if __name__=="__main__":
    n,m=map(int,input().split())
    a=list(input().split())
    a.sort()
    for i in range(len(a)):
        alpha=a[i]
        if alpha in 'aeiou':
            DFS(alpha,1,0,i)
        else:
            DFS(alpha,0,1,i)

