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

def is_palindrome_number(num):
    if(num == num[::-1]):
        for i in range(len(num)):
            if(num[0] != num[i]):
                return False
        return True
    return False
    

        
res = 0
for i in range(1, N+1):
    for j in range(1, A[i-1]+1):
        tmp = ""
        tmp += str(i) + str(j)
        if(is_palindrome_number(tmp)):
            res += 1
    
print(res)
