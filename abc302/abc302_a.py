B,A = map(int, input().split())

res = B // A
if(B % A > 0):
    res += 1

print(res)