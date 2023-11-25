"""AtCoder Beginner Contest 304 B"""
s = input()

result = ""
for i, ch in enumerate(s):
    if i >= 3:
        result += '0'
    else:
        result += ch

print(result)