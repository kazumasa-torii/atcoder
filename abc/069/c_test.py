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
6
2 7 1 8 2 8

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    def multi(x):
        cnt = 0
        while n > 1:
            if x % 2 != 0:break
            x //= 2
            cnt += 1
        return cnt
    n = int(input())
    a = list(map(int, input().split()))
    multiple = {0:0, 1:0, 2:0}
    for i in range(n):
        multiple[min(multi(a[i]), 2)] += 1
    if multiple[1]: multiple[0] += 1
    flag = True
    if multiple[0] > multiple[2] and multiple[0] - multiple[2] > 1: flag = False
    print('Yes' if flag  else 'No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
