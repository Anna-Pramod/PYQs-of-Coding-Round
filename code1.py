#Psalm 13: 5,6
#Given a square matrix, calculate the absolute diff btw the sums of its diagonals
n = int(input())
ar1 = [list(map(int,input().split(" "))) for i in range(n)]
s1,s2 = 0,0
for i in range(n):
    for j in range(n):
        if (i==j):
            s1+=ar1[i][j]
        if((i+j) == n-1):
            s2+=ar1[i][j]
r=s1-s2
if (r<0):
    print((-1)*r)
else:
    print(r) 
