n, m = map(int, input().split())
i=[]
j=[]
k=[]
for l in range(m):
    I, J, K = map(str,input().split())
    i.append(I)
    j.append(J)
    k.append(K)
basket = [0] * n
for q in range(m):
    for w in range((int(j[q])-int(i[q]))+1):
        w += int(i[q])-1
        basket[w]=int(k[q])
for e in range(n):
    print(basket[e],"",end="")