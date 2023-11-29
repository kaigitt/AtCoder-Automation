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
N = int(input())
A = [0 for _ in range(N)] #出現回数のカウント用
C = [[i+1, 0] for i in range(N)] #出現位置の格納用

B = list(map(int, input().split()))
for i in range(len(B)):
    A[B[i]-1] += 1
    
    if(A[B[i]-1] == 2):
        C[B[i]-1][1] = i+1
    
C.sort(key=lambda x: x[1])

first_elements = [row[0] for row in C]
print(*first_elements)
