basket_n, method_m = map(int, input().split())

basket_array = []
#바구니 개수 생성
for t in range(1,basket_n+1):
    basket_array.append(t)

#바구니 회전
for y in range(method_m):
    i, j, k = map(int, input().split())
    basket_array = basket_array[:i-1] + basket_array[k-1:j] + basket_array[i-1:k-1] + basket_array[j:]

print(*basket_array)

