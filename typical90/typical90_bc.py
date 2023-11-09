import itertools
import math

N, P, Q = map(int, input().split())

A = list(map(int, input().split()))

res = 0

for v in itertools.combinations(A, 5):
    a, b, c, d, e = v
    if a % P * b % P * c % P * d % P * e % P == Q:  # (a*b*c*d*e)%PだとTLEになる
        res += 1

print(res)    