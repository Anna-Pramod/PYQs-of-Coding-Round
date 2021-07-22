#Psalm 13: 5,6
#Balancing Pipes
n,m,r = map(int,input().split(" "))
N = list(map(int,input().split(" ")))
M = list(map(int,input().split(" ")))

act_sum_n = sum(N) - (n*r)
act_sum_m = sum(M) - (m*r)

if (act_sum_n > act_sum_m):
    d = act_sum_n - act_sum_m + r
    print((-1)*d)
elif(act_sum_m > act_sum_n):
    d = act_sum_m - act_sum_n + r
    print(d)
else:
    print("BALANCED")