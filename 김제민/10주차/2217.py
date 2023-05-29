import sys
input = sys.stdin.readline
n = int(input().rstrip())
rope = list(int(input().rstrip()) for _ in range(n))
rope.sort()
weight = []
for i in range(n):
    weight.append(rope[i] * (n - i))
print(max(weight))