# count number of Odd and Even elements in array
def countOddEven(arr):
    odd=0
    even=0
    for i in arr:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
arr=list(map(int,input().split()))
print(countOddEven(arr))