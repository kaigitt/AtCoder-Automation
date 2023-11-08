N = int(input())
S = input()

res = -1

for i in range(N-2):
    if(S[i:i+3] == "ABC"):
        res = i+1
        break

print(res)
    