test = []
result = []


for i in range(int(input())):
    money = int(input())
    test.append(money)

for j in test:
    quarter = j//25
    dime = (j%25)//10
    nickel = ((j%25)%10)//5
    penny = (((j%25)%10))%5
    result.append(quarter)
    result.append(dime)
    result.append(nickel)
    result.append(penny)



print(*result[:4])
print(*result[4:8])
print(*result[8:])



