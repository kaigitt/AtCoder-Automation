import math
A,B = map(int, input().split())
res = math.lcm(A, B)
if(res > 10 ** 18):
    print("Large")
else:
    print(res)