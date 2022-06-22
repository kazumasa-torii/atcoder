"""
for 一つで考える
"""
from math import sqrt
import sys
from typing import List
input = sys.stdin.readline

def main():
    N, D = map(int, input().split())
    li = []
    for _ in range(N):
        li.append(list(map(int, input().split())))

    ctr = 0
    for i in range(N):
        for j in range(1+i, N):
            summ = 0
            for k in range(D):
                summ += (li[i][k] - li[j][k]) ** 2
            sqrtsumm = sqrt(summ)

            print(sqrtsumm, int(sqrtsumm))
            if int(sqrtsumm) == sqrtsumm:
                ctr += 1
    print(ctr)

    return

main()
