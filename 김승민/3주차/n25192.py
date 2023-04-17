import sys

user_set = set()
count = 0

for i in range(int(input())):
    user = sys.stdin.readline().rstrip()
    if((user != 'ENTER') and (user != 'enter')):
        if user not in user_set:
            user_set.add(user)
            count += 1
    elif ((user == 'ENTER') or (user == 'enter')):
        user_set.clear()

print(count)