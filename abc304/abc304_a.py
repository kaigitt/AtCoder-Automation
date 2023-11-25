N = int(input())

min_i = 10**9

names = []
ages = []

for i in range(N):
    name, age = input().split()
    names.append(name)
    ages.append(age)

tmp = 0
for i in range(N):
    if(int(ages[i]) < min_i):
        min_i = int(ages[i])
        tmp = i

for i in range(N):
    print(names[(i+tmp) % N])
    
