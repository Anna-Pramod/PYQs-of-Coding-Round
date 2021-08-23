#Psalm 13: 5,6
#Write a program to convert a string written as JAVA variable to C++ variable and vice-versa. 
#Input : this_is_a_variable Output: thisIsAVariable
s=input()
def tojava(s):
    j = s.split("_")
    n = [j[0]]
    for i in range(1,len(j)):
        n.append(j[i].title())
    print("".join(n))

def tocpp(s):
    c = []
    for i in s:
        if (i.isupper()!=True):
            c.append(i)
        else:
            c.append("_")
            c.append(i.lower())
    print("".join(c))
        
if("_" in s):
    tojava(s)
else:
    tocpp(s)
