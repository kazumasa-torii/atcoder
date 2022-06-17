"""
ただし2つの数があるので二重で引いてしまう可能性もある
そこで最小公倍数を求めてそこの倍数分の数をプラスする

その後に同じ作業をA未満の数でも行って答えから差し引けば区間が求まる

1.全体から割りたい数を削除する(全体//割りたい数)
1.同じ作業をもう一度行う
1.CとDの最小公倍数を求めて割り切れる数をプラスする
    * CとDで割り切れる数が同じ数の場合がある
1.A未満で同じ作業を行い答えから差し引く 
"""

import sys
import math
from typing import List
input = sys.stdin.readline

def lcm(a, b):
    return a * b // math.gcd (a, b)

def main():
    A, B, C, D = map(int, input().split())
    ans = B - (B//C) - (B//D) + (B//lcm(C, D))
    A -= 1
    ans -= A - (A//C) - (A//D) + (A//lcm(C, D))
    print(ans)
    return

main()
