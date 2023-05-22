import sys
input=sys.stdin.readline
n,k,q,m=map(int,input().split())
k_n=set(map(int,input().split()))
q_n=set(map(int,input().split()))
for y in range(m):
    s,e=map(int,input().split())
    all_n=set(i for i in range(s,e+1))
    non=set()
    q_m=set()
    k_m=set()
    q_n = q_n - k_n
    for x in range(k):
        a=k_n.pop()
        k_m.add(a)
        if a in all_n:
            non.add(a)
    t=len(q_n)
    for j in range(t):
        a=q_n.pop()
        q_m.add(a)
        a_a=a
        while a_a<=e:
            all_n.discard(a_a)
            a_a+=a
    non.update(all_n)
    k_n=k_m
    q_n=q_m
    print(len(non))