import sys
input = sys.stdin.readline
n = int(input().rstrip())
stack = []
for i in range(n):
    comm = list(input().rstrip().split())
    if comm[0] == 'push':
        stack.append(int(comm[1]))
    elif comm[0] == 'pop':
        if len(stack) > 0: 
            print(stack.pop(-1))
        else:
            print(-1)
    elif comm[0] == 'size':
        print(len(stack))
    elif comm[0] == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif comm[0] == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
