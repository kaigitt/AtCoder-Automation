N = int(input())

user_set = set()

for i in range(N):
    user_name = input()
    if(user_name in user_set):
        pass
    else:
        print(i+1)
        user_set.add(user_name)
