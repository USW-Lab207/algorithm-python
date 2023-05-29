import sys
input = sys.stdin.readline
s = list(input())
i = 0
k = 0
switch = []
while i < len(s):
    if s[i] == '<':
        i += 1
        while s[i] != '>':
            i += 1
        i += 1
    elif s[i].isalnum():
        k = i
        while i < len(s) and s[i].isalnum():
            i += 1
        switch = s[k:i]
        switch.reverse()
        s[k:i] = switch
    else:
        i += 1

print(*s, sep='')