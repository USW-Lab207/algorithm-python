import sys
from collections import deque
input=sys.stdin.readline
arr=deque()
def push_front(x):
    arr.appendleft(x)
def push_back(x):
    arr.append(x)
def pop_front():
    if len(arr)<1:
        print(-1)
    else:
        print(arr.popleft())
def pop_back():
    if len(arr)<1:
        print(-1)
    else:
        print(arr.pop())
def size():
    print(len(arr))
def empty():
    if len(arr)<1:
        print(1)
    else:
        print(0)
def front():
    if len(arr)<1:
        print(-1)
    else:
        print(arr[0])
def back():
    if len(arr)<1:
        print(-1)
    else:
        print(arr[-1])
n=int(input())
for i in range(n):
    s=input().strip()
    if 'push_front' in s:
        push_front(int(s[11:]))
    elif 'push_back' in s:
        push_back(int(s[10:]))
    elif s=='pop_front':
        pop_front()
    elif s=='pop_back':
        pop_back()
    elif s=='size':
        size()
    elif s=='empty':
        empty()
    elif s=='front':
        front()
    else:
        back()