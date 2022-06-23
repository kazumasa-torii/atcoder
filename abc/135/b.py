"""
for 一つで考える
"""
import sys
from copy import deepcopy
from typing import List
input = sys.stdin.readline

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p_sort = deepcopy(p)
    p_sort.sort()
    for i in range(n):
        tmp = p[i]
        for j in range(n):
            pt = deepcopy(p)
            pt[i] = pt[j]
            pt[j] = tmp
            if p_sort == pt:
                print('YES')
                sys.exit()
    print('NO')

    return

main()
