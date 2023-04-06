"""

[문제 링크](https://www.acmicpc.net/problem/5430)

### 성능 요약

메모리: 41828 KB, 시간: 228 ms

### 분류

구현, 자료 구조, 문자열, 파싱, 덱
"""
# [Gold V] AC - 5430

from collections import deque
import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    err=0
    p=input()
    n=int(input())
    arr=deque(input().rstrip()[1:-1].split(","))
    cnt=0
    if n == 0:
        arr=deque([])

    for i in range(len(p)):
        if p[i] == "R":
            cnt += 1
        elif p[i] == "D":
            if cnt % 2 == 0:
                if arr:
                    arr.popleft()
                else:
                    print("error")
                    err=1
                    break
            else:
                if arr:
                    arr.pop()
                else:
                    print("error")
                    err=1
                    break
    if err==0:
        if cnt % 2 == 0:
            print("[" + ",".join(arr) + "]")
        else:
            arr.reverse()
            print("[" + ",".join(arr) + "]")