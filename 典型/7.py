import sys
from bisect import bisect_left
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
a = sorted(A)
Q = int(input())
for _ in range(Q):
    tmp = int(input())
    index = bisect_left(a, tmp)
    if index - 1 < 0:
        index = 0
    else:
        index -= 1
    print(min(abs(a[index] - tmp), abs(a[index+1] - tmp)))

"""
答えのコード
二分探索しているっぽいけどちょっと解読が必要
"""
n = int(input())
a = list(map(int, input().split()))
q = int(input())

a.sort()

for i in range(q):
    b = int(input())
    l, r = 0, n-1
    while r - l > 1:
        m = l + (r - l)//2
        if b < a[m]:
            r = m
        else:
            l = m
    print(min(abs(b-a[l]), abs(b-a[r])))
