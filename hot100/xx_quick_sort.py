
def partition(num,left,right):
    v=num[left]
    i,j=left,right
    while i<j:
        while i<j and num[j]>=v:
            j-=1
        num[i]=num[j]
        while i<j and num[i]<=v:
            i+=1
        num[j]=num[i]
    num[i]=v
    return i

def quick_sort(num,left,right):
    if left<right:
        index=partition(num,left,right)
        quick_sort(num,left,index)
        quick_sort(num,index+1,right)

arr=[0,9,3,8,6,5]
quick_sort(arr,0,len(arr)-1)
print(arr)

