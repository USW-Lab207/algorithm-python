import sys
input = sys.stdin.readline
n, k = map(int, input().rstrip().split())
sk = list(map(int, input().rstrip().split()))
dn = list(map(int, input().rstrip().split()))
for j in range(k):
    s = [0] * n
    for i in range(n):
        s[dn[i] - 1] = sk[i]
    sk = s
print(*sk)