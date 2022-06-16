"""
エラトステネスの篩
素数数えるやつ

基本は素数を見つけてその素数で削除できるやつは削除するみたいな対応
"""

import sys
from typing import List
def main():
    input = sys.stdin.readline
    N: int = int(input())

    # テーブルを用意
    is_prime: List[int] = [True] * (N+1)

    # 0, 1は初期値で落としておく
    is_prime[0], is_prime[1] = False, False

    # ふるい
    for p in range(2, N+1):

        # メモですでに対応済みのやつ
        if not is_prime[p]:
            continue

        # p以外でpの倍数であるのもはスキップしてふるいから落としておく
        q = p * 2
        while q <= N:
            is_prime[q] = False
            q += p
    print(sum(is_prime))
    return

if __name__ == '__main__':
    main()
