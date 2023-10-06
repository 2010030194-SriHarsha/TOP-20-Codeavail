# def multiplicationTable(n):
#     for i in range(1,11):
#         print(f"{n} * {i} = {n*i}")
# n=int(input())
# multiplicationTable(n)

# using recursion
def multiplicationTable2(n,i=1):
    if i<=10:
        print(f"{n} * {i} = {n*i}")
        multiplicationTable2(n,i+1)
n=int(input())
multiplicationTable2(n)