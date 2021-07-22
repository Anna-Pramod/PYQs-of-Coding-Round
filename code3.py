#Psalm 13: 5,6
a = int(input())
def twodigit(a):
    stack = []
    for i in range(9,1,-1):
        while(a%i==0):
            a=a//i
            stack.append(i)
        if (a==1):
            break
    b=0
    if (a==1):
        while (stack):
            b = (b*10) + stack.pop()
        print (b)
    else:
        print(-1)
if(a<10):
    print(a+10)
else:
    twodigit(a)

    