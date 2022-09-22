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
5
1 1 2 1 2

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    def choose(n):
        return n * (n-1) // 2

    n = int(input())
    a = list(map(lambda x: int(x) - 1, input().split()))
    
    cnt = [0] * n
    for i in range(n): cnt[a[i]] += 1
    tot = 0
    for i in range(n): tot += choose(cnt[i])
    for i in range(n):
        ans = tot
        ans -= choose(cnt[a[i]])
        ans += choose(cnt[a[i]] - 1)
        print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
