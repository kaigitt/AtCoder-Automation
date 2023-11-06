import math

B = int(input())

res = 1
flag = False

while res <= 15:
    if(res ** res == B):
        flag = True
        break
    res += 1

if(flag):
    print(res)
else:
    print(-1)