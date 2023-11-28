n = int(input())
s = input()
t = 0
a = 0
for i in range(0, n):
    if s[i] == 'T':
        t += 1
    else:
        a += 1
        
if t > a:
    print('T')
elif t < a:
    print('A')
elif s[-1] == 'A':
    print('T')
else:
    print('A')