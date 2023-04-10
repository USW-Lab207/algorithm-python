people, price = map(int,input().split())

score = list(map(int,input().split()))

score.sort(reverse=True)

print(score[price-1])