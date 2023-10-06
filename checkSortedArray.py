def checkArray(arr):
    n=len(arr)
    i=0
    j=1
    while j<n:
        if arr[i]<arr[j]:
            i+=1
            j+=1
        else:
            return False
    return True
arr=list(map(int,input().split()))
print(checkArray(arr))