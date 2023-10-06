def reverseNum(n):
    rev=0
    while n:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    return rev
n=int(input())
print(reverseNum(n))