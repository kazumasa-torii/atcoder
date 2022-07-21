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
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
7 3
1 2 1 2 3 3 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import Counter
def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    cnt = Counter(c[:k])
    ans = len(cnt)
    for i in range(k, n):
        l = c[i-k]
        r = c[i]
        cnt[l] -= 1
        cnt[r] += 1
        if cnt[l] == 0:
            del cnt[l]
        ans = max(ans, len(cnt))
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
