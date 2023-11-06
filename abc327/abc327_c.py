
A = [[int(x) for x in input().split()] for i in range(9)]

flag = True

# 1つ目のルール
for i in range(9):
    set_N = set()
    for j in range(9):
        if(1 <= A[i][j] and A[i][j] <= 9):
            set_N.add(A[i][j])
    if(not(len(set_N) == 9)):
        flag = False
        break


# 2つ目のルール
for i in range(9):
    set_N = set()
    for j in range(9):
        if(1 <= A[j][i] and A[j][i] <= 9):
            set_N.add(A[j][i])
    if(not(len(set_N) == 9)):
        flag = False
        break
        
# 3つ目のルール
for i in range(0,9,3):
    for j in range(0,9,3):
        set_N = set()
        for k in range(i, i+3):
            for l in range(j, j+3):
                if(1 <= A[k][l] and A[k][l] <= 9):
                    set_N.add(A[k][l])
        if(not(len(set_N) == 9)):
            flag = False
            break
        


# 出力

if(flag):
    print("Yes")
else:
    print("No")