n, k = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
x.reverse()
cut = []
for i in range(k):
    cut.append(x[i])
cut.sort()
print(cut[0])