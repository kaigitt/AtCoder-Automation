"""
N = int(input())
N,M = map(int, input().split())

A = []
flag = False

print("Yes" if flag else "No")
""" 
N,M = map(int, input().split())
A = list(map(int, input().split()))

res = 0
for i in range(N):
    if(A[i] >= M):
        res += 1

print(res)