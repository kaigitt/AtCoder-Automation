# coding: utf-8
# Your code here!

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

H, W = map(int, input().split())
A = []
for i in range(H):
    tmp = input()
    A.append(list(tmp))

target = ['s', 'n', 'u', 'k', 'e']
d = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

res = []
for i in range(H):
    for j in range(W):
        for k in range(8):
            di = i
            dj = j
            flag = True
            
            for l in range(len(target)):
                if(0 <= di and 0 <= dj and di < H and dj < W):
                    if(A[di][dj] != target[l]):
                        flag = False
                        continue
                    else:
                        t = []
                        t.append(di)
                        t.append(dj)
                        res.append(t)
                else:
                    flag = False
                
                di += d[k][0]
                dj += d[k][1]
            if(flag):
                for q in res:
                    print(q[0]+1, q[1]+1)
                exit()
            else:
                res = []
