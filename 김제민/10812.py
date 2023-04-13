n, m =  map(int, input().split())
basket = [p for p in range(n+1)]
for z in range(m):
    i, j, k = map(int, input().split())
    start = basket[i:k]
    end = basket[k:j+1]
    basket[i:j+1] = end + start

print(*basket[1:])