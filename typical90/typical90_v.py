import math

A,B,C = map(int, input().split())

gcd_3 = math.gcd(A, B, C)

res = ((A // gcd_3) - 1) + ((B // gcd_3) - 1) +((C // gcd_3) - 1)

print(res)