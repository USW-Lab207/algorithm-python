import sys
input=sys.stdin.readline
list=[]
def push(x):
    list.append(x)
def pop():
    if list==[]:
        print(-1)
    else:
        print(list.pop())
def size():
    print(len(list))
def empty():
    if list==[]:
        print(1)
    else:
        print(0)
def top():
    if list==[]:
        print(-1)
    else:
        print(list[-1])
n=int(input())
for i in range(n):
    s=input().split()
    if s[0]=='push':
        push(int(s[1]))
    elif s[0]=='pop':
        pop()
    elif s[0]=='empty':
        empty()
    elif s[0]=='size':
        size()
    elif s[0]=='top':
        top()