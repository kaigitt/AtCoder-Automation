import math

"""
L, R = map(int, input().split())
N, M = map(int, input().split())
MOD = 10**9 + 7

d = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 上下左右の方向

A = list(map(int, input().split()))
res = 0
for i in range(N):
    res += A[i]
print(res)

if(flag):
    print("Yes")
else:
    print("No")

"""
A = list(map(int, input().split()))

res = 0
for i in range(len(A)):
    if(A[i] == 1):
        res += (2 ** i)
    
print(res)
        
        


