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
S = []
for i in range(H):
    tmp = list(input())
    S.append(tmp)
    
d = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 上下左右の方向

x = 0
y = 0
for i in range(H):
    for j in range(W):
        if(S[i][j] == "."):
            find_count = 0
            for k in range(4):
                di = i + d[k][0]
                dj = j + d[k][1]
                if(0 <= di and 0 <= dj and di < H and dj < W):
                    if(S[di][dj] == "#"):
                        find_count += 1
            if(find_count >= 2):
                y = i+1
                x = j+1
                break

print(y, x)
        
        
        
        


