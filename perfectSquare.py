def perfectSquare(n):
    low=1
    high=n
    while low<=high:
        midd=(low+high)//2
        if midd*midd==n:
            return midd
        elif midd*midd<=n:
            low=midd+1
        else:
            high=midd-1
n=int(input())
if perfectSquare(n):
    print(True)
else:
    print(False)