import sys
input = sys.stdin.readline
word = list(input().rstrip())
key = list(input().rstrip())
check = []
i = 0
while i < len(word):
    a = word[i]
    if a.isdigit():
        word.pop(i)
        i -= 1
    i += 1
c = 1
word.append(0)
for k in range(len(word) - 1):
    if word[k] == key[0]:
        check = word[k:k + len(key)]
        if check == key:
            c *= 0
if c == 0:
    print(1)
else:
    print(0)