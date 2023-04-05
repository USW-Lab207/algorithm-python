N_basket, M_method = map(int, input().split())

basket_array = []
for t in range(N_basket):
    basket_array.append(0)


for t in range(M_method):
    i, j, k = map(int, input().split())
    for _ in range(i-1, j):
        basket_array[_] = k

for t in range(len(basket_array)):
    print(basket_array[t], end=" ")

#젠장 실행하는 법 모르겠다 물어보자 (4/5)