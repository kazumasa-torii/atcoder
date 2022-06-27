"""
for 一つで考える
"""
import sys
from typing import List
input = sys.stdin.readline

def main():
    n, k, q = map(int, input().split())
    a = [i-1 for i in map(int, input().split())]
    l = [i-1 for i in map(int, input().split())]

    for i in l:
        target = a[i]
        flag = True
        if target + 1 == n:
            continue
        for j in a:
            if j == target + 1:
                flag = False
                continue
        if flag:
            a[i] += 1
    for i in range(k):
        a[i] += 1
    print(*a)
    return

main()
