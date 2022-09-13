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

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import defaultdict
def main():
    n = int(input())
    dic = defaultdict(int)

    for _ in range(n):
        tmp = input()
        dic[tmp] += 1
    nums = []
    for _, i in enumerate(dic):
        nums.append(dic[i])
    m = max(nums)

    dic_sort = sorted(dic.keys(), key=lambda x: x)

    for i in dic_sort:
        if dic[i] == m:
            print(i)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')