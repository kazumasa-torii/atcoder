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
5 5
1 3
4 5
2 3
2 4
1 4

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n,m=map(int,input().split())
    s=[[] for i in range(n)]
    for i in range(m) :
        a,b=map(int,input().split())
        s[a-1].append(b-1)

    for i in s[0] :
        if n-1 in s[i] :
            print("POSSIBLE")
            exit()
    
    print("IMPOSSIBLE")
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
