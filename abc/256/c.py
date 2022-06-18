"""
abc
def
ghi

計算する量をどれだけ落とせるかが問題
どこを計算したら求まるかをもっと理解していたら行けた
"""

import sys
from typing import List
input = sys.stdin.readline

def main():
    li = list(map(int, input().split()))

    ans = 0
    for a in range(1, 31):
        for b in range(1, 31):
            for d in range(1, 31):
                for e in range(1, 31):
                    c = li[0] - a - b
                    f = li[1] - d - e
                    g = li[3] - a - d
                    h = li[4] - b - e
                    i = li[5] - c - f
                    if min(c,f,g,h,i) > 0 and g + h + i == li[2]: ans += 1

    print(ans)
    return

main()
