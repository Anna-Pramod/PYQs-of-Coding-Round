#Psalm 13: 5,6
#SPIRAL TRAVERSAL OF A MATRIX
n=int(input())
mat = [list(map(int,input().split(" "))) for _ in range(n)]

top = left = 0
down = right = n-1
dir = 0

while(top<=down and left<=right):

    if (dir==0):
        for i in range(left,right+1):
            print(mat[top][i],end=" ")
        top +=1
    elif (dir==1):
        for i in range(top,down+1):
            print(mat[i][right],end=" ")
        right -=1
    elif (dir==2):
        for i in range(right,left-1,-1):
            print(mat[down][i],end=" ")
        down -=1
    elif (dir==3):
        for i in range(down,top-1,-1):
            print(mat[i][left],end=" ")
        left +=1
    
    dir = (dir+1)%n

