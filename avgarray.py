def avgArray(arr):
    n=len(arr)
    summ=0
    avg=0
    for i in arr:
        summ+=i
    avg=summ/n
    return avg
arr=list(map(int,input().split()))
print(avgArray(arr))