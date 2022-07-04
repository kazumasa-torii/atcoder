"""
sortして愚直に全探索できるか考える
その後に難しそうであれば下記アルゴリズムを考える

共通
全探索,二部探索,累積和,いもす法,順列全探索,区間スケジューリング,貪欲法

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
8
199 100 200 400 300 500 600 200

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import defaultdict
def main():
    num = 200
    ans = 0
    N = int(input())
    A = list(map(int, input().split()))
    dic = defaultdict(int)
    for i in range(N):
        dic[A[i] % num] += 1
    for _, i in enumerate(dic):
        ans += (dic[i] * (dic[i] - 1)) / 2
    print(int(ans))
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
