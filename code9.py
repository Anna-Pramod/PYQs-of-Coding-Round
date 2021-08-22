#Psalm 13:5,6
#Rotating a 2D square matrix clockwise 90deg

n=int(input())
mat = [list(map(int,input().split(" "))) for _ in range(n)]
for i in range(n):
    for j in range(n):
        mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    print(" ".join([str(s) for s in mat[i][::-1]]))