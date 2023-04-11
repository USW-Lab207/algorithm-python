n, m = map(int, input().split())
basket = [0] * (n+1)
for l in range(m):
    i, j, k = map(int,input().split())
    for w in range(i, j+1):
        basket[w] = k

print(*basket[1:])