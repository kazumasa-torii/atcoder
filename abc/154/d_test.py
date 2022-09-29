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
from re import I
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
5 3
1 2 2 4 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    def exNum(x):
        return (((x + 1) * x) // 2) / x
    n, k = map(int, input().split())
    a = list(map(lambda x: exNum(int(x)), input().split()))
    ans = 0
    acc = [0]
    for i in a:
        acc.append(acc[-1]+i)
    for i in range(n+1):
        l = i
        r = i+k
        if r > n:break
        ans = max(ans, acc[r] - acc[l])
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
