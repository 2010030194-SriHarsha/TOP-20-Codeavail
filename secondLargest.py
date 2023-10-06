def secondLargest(arr):
    arr=sorted(arr)
    return arr[-2]
arr=list(map(int,input().split()))
print(secondLargest(arr))