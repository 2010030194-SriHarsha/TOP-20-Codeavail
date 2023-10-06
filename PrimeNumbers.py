# Print the all the prime numbers less than 'n'
def sieve(n):
    primes=[True]*(n+1)
    primes[0]=primes[1]=False
    for i in range(2,int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i,n+1,i):
                primes[j]=False
    return [i for i in range(2,n) if primes[i]]
n=int(input())
print(sieve(n))

#check the given number is prime or not
def checkPrime(n):
    if n>1:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    return False
n=int(input())
print(checkPrime(n))