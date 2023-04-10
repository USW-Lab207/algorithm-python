people, price = map(int,input().split())

point = list(map(int,input().split()))

point.sort(reverse=True)

print(point[price-1])