"""
直前の数字が大事であってそれ以外はあまり気にする必要性がなかった
貪欲に求めていく形にする
"""

import sys
from typing import List
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))

    flag = True
    tmp = -999
    for i in range(n):
        if tmp <= a[i] - 1:
            tmp = a[i] - 1
        elif tmp <= a[i]:
            tmp = a[i]
        else:
            print('No')
            sys.exit()
    print('Yes')
    return

main()
