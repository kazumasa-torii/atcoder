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
8
7 3 5 4 2 1 6 8
3 8 2 5 4 6 7 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

import itertools
def main():
    n = int(input())
    nums = [i for i in range(1, n+1)]
    ptr = list(itertools.permutations(nums, n))
    ptr.sort()
    ans = 0
    for _ in range(2):
        tmp = list(map(int, input().split()))
        for i in range(len(ptr)):
            flag = True
            for x, y in zip(tmp, ptr[i]):
                if x != y:
                    flag = False
                    break
            if flag: break
        ans = abs(ans - i)
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
