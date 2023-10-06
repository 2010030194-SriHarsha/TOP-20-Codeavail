# Using formulae
def sumOfSquares(n):
    return int((n*(n+1)*(2*n+1))/6)
n=int(input())
print(sumOfSquares(n))

# using loop
def sumOfSquares2(n):
    ans=0
    for i in range(1,n+1):
        ans+=i**2
    return ans
n=int(input())
print(sumOfSquares2(n))