import sys
input = sys.stdin.readline
n = int(input().rstrip())
stack = list()
for i in range(n):
    comm = list(map(str, input().rstrip().split()))
    if comm[0] == 'push_front':
        a = [int(comm[1])]
        stack = a + stack
    if comm[0] == 'push_back':
        stack.append(int(comm[1]))
    if comm[0] == 'pop_front':
        try:
            print(stack.pop(0))
        except:
            print(-1)
    if comm[0] == 'pop_back':
        try:
            print(stack.pop(-1))
        except:
            print(-1)
    if comm[0] == 'size':
        print(len(stack))
    if comm[0] == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1) 
    if comm[0] == 'front':
        try:
            print(stack[0])
        except:
            print(-1)
    if comm[0] == 'back':
        try:
            print(stack[-1])
        except:
            print(-1)