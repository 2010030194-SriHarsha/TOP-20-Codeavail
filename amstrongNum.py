# check the given number is Amstrong Number or not
def checkAmstrong(n):
    temp=n
    p=0
    while n:
        rem=n%10
        p=p+(rem**3)
        n=n//10
    return temp==p
n=int(input())
print(checkAmstrong(n))