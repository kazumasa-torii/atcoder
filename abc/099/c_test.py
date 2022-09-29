
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
11 3
7 3 1 8 4 6 2 5 6 3 4

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    def judge(n, i):
        i -= 1
        cnt = 1
        while n > 0:
            n -= i
            cnt += 1
        return cnt
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if n == k: exit(print(1))
    print(judge(n-k, k))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
