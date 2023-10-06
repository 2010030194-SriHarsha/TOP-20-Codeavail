def palindromeNum(n):
    rev=0
    temp=n
    while n:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    return rev==temp
n=int(input())
print(palindromeNum(n))