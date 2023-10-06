def sortArray(arr):
    count=0
    for i in arr:
        if i==0:
            count+=1
    for i in range(count):
        arr[i]=0
    for i in range(count,len(arr)):
        arr[i]=1
    return arr
arr=list(map(int,input().split()))
print(sortArray(arr))