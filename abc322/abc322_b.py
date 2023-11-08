N, M = map(int, input().split())
S = input()
T = input()

def is_prefix(S, T):
    for i in range(len(S)):
        if(S[i] != T[i]):
            return False
    return True
    
def is_suffix(S, T):
    
    for i in range(len(S)):
        if(S[::-1][i] != T[::-1][i]):
            return False
    return True
    
res = 0

if(is_prefix(S,T)):
    if(is_suffix(S,T)):
        res = 0
    else:
        res = 1
elif(is_suffix(S,T)):
    if(not is_prefix(S,T)):
            res = 2
else:
    res = 3
    
print(res)