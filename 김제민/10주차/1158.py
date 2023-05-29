import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
circle = [i for i in range(1, n+1)]
index = 0
result = []
while len(circle) > 0:
    index = (index + k - 1) % len(circle)
    result.append(circle.pop(index))

print('<', end='')
for k in range(n-1):
    print(result[k], ',', sep='', end=' ')
print(result[-1], '>', sep='')