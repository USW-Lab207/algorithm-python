import sys

S = sys.stdin.readline().rstrip()
keyword = sys.stdin.readline().rstrip()
tmp = []

for i in S:
    if(i.isalpha()):
        tmp.append(i)

str = ''.join(tmp)

if keyword in str :
    print(1)
else:
    print(0)
