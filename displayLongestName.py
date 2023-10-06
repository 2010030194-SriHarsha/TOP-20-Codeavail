def display(names):
    res=max(names,key=len)
    return res
names=input().split()
print(display(names))

# using Loops
def display2(names):
    res=""
    maxx=-1
    for i in names:
        if len(i)>maxx:
            maxx=len(i)
            res=i
    return res
names=input().split()
print(display2(names))