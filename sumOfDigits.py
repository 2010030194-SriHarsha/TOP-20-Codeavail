def sumOfDigits(n):
    ans=0
    n=str(n)
    for i in range(len(n)):
        ans+=int(n[i])
    return ans
n=int(input())
print(sumOfDigits(n))