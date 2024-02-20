def Qsort(lt,rt):
    if lt<rt:
        pivot=arr[rt]
        pos=lt
        for i in range(lt,rt):
            if arr[i]<=pivot:
                arr[i],arr[pos]=arr[pos],arr[i]
                pos+=1
        arr[pos],arr[rt]=arr[rt],arr[pos]

        Qsort(lt,pos-1)
        Qsort(pos+1,rt)

if __name__=="__main__":
    arr=[23,41,23,1,234,533,231,10]
    print(arr)
    Qsort(0,7)
    print(arr)
    