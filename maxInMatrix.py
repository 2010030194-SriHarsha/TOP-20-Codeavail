def maxElement(mat,r,c):
    maxx=0
    for i in range(r):
        for j in range(c):
            maxx=max(maxx,mat[i][j])
    return maxx
r,c=list(map(int,input().split()))
mat=[]
for i in range(r):
    mat.append(list(map(int,input().split())))
print(maxElement(mat,r,c))