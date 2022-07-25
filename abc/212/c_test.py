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
6 8
82 76 82 82 71 70
17 39 67 2 45 35 22 24

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

import math
sys.setrecursionlimit(3000)
def main():
    def isOK(index: int, key:int) -> bool:
        if b[index] >= key: return True
        else: return False

    def binary_search(key: int) -> int:
        left: int = -1
        right: int = len(b)
        while right - left > 1:
            mid: int = math.ceil(left + (right - left) / 2)
            if isOK(mid, key): right = mid
            else: left = mid
        return right
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    b.sort()
    ans = 10 ** 10

    for i in a:
        r = binary_search(i)
        l = r - 1
        if r < len(b): ans = min(ans, abs(i-b[r]))
        if l >= 0: ans = min(ans, abs(i-b[l]))
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
