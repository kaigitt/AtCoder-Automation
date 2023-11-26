"""
N = int(input())
N,M = map(int, input().split())

A = []
flag = False

print("Yes" if flag else "No")
""" 
N,L,R = map(int, input().split())
A = list(map(int, input().split()))

res = []
for i in range(N):
    if(A[i] < L):
        res.append(L)
    elif(R < A[i]):
        res.append(R)
    else:
        res.append(A[i])

print(*res)
        