#Psalm 13:5,6
#"LENGTH OF LONNGEST VALID SUBSTRING"

s = input()
stack=[-1]
result=0
for i,val in enumerate(s):
    if val =="(":
        stack.append(i)
    else:
        if(stack):
            stack.pop()
        if(stack):
            result = max(result, i-stack[len(stack)-1])
        else:
            stack.append(i)
print (result)