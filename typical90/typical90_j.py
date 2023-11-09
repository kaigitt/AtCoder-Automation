N = int(input())

class_1 = []
class_2 = []

class_1.append(0)
class_2.append(0)

for i in range(1, N+1):
    c, p = map(int, input().split())
    if(c == 1):
        class_1.append(p + class_1[i-1])
        class_2.append(class_2[i-1])
    else:
        class_2.append(p + class_2[i-1])
        class_1.append(class_1[i-1])


Q = int(input())

for i in range(Q):
    l, r = map(int, input().split())
    print((class_1[r] - class_1[l-1]), (class_2[r] - class_2[l-1]))