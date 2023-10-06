# using Recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
n=int(input())
print(factorial(n))

# using loop
def factorial2(n):
    fact=1
    if n==0:
        return fact
    for i in range(2,n+1):
        fact=fact*i
    return fact
n=int(input())
print(factorial2(n))

# using 1-D array
def factorial3(n):
    if n==0 or n==1:
        return 1
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]*i
    return dp[n]
n=int(input())
print(factorial3(n))