"""
sortして愚直に全探索できるか考える
その後に難しそうであれば下記アルゴリズムを考える

共通
全探索,二部探索,累積和,いもす法,順列全探索,区間スケジューリング,貪欲法,鳩の巣原理

グラフ関係
DFS,BFS,ダイクストラ法,ワーシャルフロイド法,トポロジカルソート

DP
区間,bit,ナップサック,桁

数学
約数,素数判定法,mod,組み合わせ,幾何

その他
クラスカル法,木,Union-find
"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
99992

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
            if i * i > n:
                break
            if n % i == 0:
                return False
        return n != 1
    n = int(input())
    while True:
        if is_prime(n):break
        n += 1
    print(n)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
