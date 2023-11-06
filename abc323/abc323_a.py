S = input()

flag = True

for i in range(1, len(S)):
    if(i % 2 != 0):
        if(S[i] != "0"):
            flag = False

if(flag):
    print("Yes")
else:
    print("No")