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
from xml.dom.minidom import Node

_INPUT = """\
2000 20000000

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, y = map(int, input().split())
    man = 10000
    fsen = 5000
    sen = 1000

    for i in range(n+1):
        for j in range(n+1):
            if i + j > n: break
            if (man * i) + (fsen * j) + (sen * (n-(i+j))) == y:exit(print(i, j, (n-(i+j))))
    print(-1, -1, -1)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
