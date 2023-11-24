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
N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

maxN = A[0]

for i in range(N):
    if(A[i] != maxN):
        print(A[i])
        break