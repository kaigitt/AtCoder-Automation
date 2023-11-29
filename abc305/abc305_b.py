import math

"""
L, R = map(int, input().split())
N, M = map(int, input().split())
MOD = 10**9 + 7

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
p,q = input().split()
if(p > q):
    tmp = p
    p = q
    q = tmp

A = [3, 1, 4, 1, 5, 9]

total = 0
for i in range(ord(p)-65, ord(q)-65):
    total += A[i]

print(total)