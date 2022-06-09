"""
p > q を使用して k = p * qの3乗 となるN以下の整数を答える問題
qを3乗するからqは大きくても 3√10の18乗 = 10の6乗 よりは小さくなる
なのでqを全探索します。

1.素数列挙を行う
1.pを小さい順に2から並べて計算していく
1.p * qの3乗 が目的の数値より大きくなったらその素数の探索は終了（枝切り）
1.最後にansを答える
"""
import sys
from typing import List
input = sys.stdin.readline

# 素数列挙
def enum_primes(n: int) -> List[int]:
    prime_flag: List[int] = [1] * (n + 1)
    prime_flag[0] = 0
    prime_flag[1] = 0

    i: int = 2
    while i * i <= n:
        if prime_flag[i]:
            for j in range(2 * i, n + 1, i):
                prime_flag[j] = 0
        i += 1

    return [i for i in range(n+1) if prime_flag[i]]

# メインの処理
def main():
    N: int = int(input())
    ans: int = 0
    prims: List[int] = enum_primes(10 ** 6 + 5)
    M: int = len(prims)

    for i in range(M):
        # 先に3乗の計算をしておく
        t: int = prims[i] ** 3
        for j in range(i):
            if t * prims[j] > N:
                break
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
