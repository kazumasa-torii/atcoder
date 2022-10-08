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
4
1 6 8 9

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n == 2:
        even = False
        odd  = False
        if a[0] % 2 == 0:even = True
        else: odd = True
        if a[1] % 2 == 0:even = True
        else: odd = True
        if even and odd: exit(print(-1))
        else: exit(print(sum(a)))
    ma = max(a)
    if ma % 2 == 0:
        for i in reversed(a[:n-1]):
            if i % 2 == 0:
                one = ma+i
                break
        two = 0
        for i in reversed(a[:n-1]):
            if i % 2 == 1:
                two += i
                break
        for i in reversed(a[:n-1]):
            if i % 2 == 1 and two != i:
                two += i
                break
        print(max(one, two))
    else:
        for i in reversed(a[:n-1]):
            if i % 2 == 1:
                one = ma+i
                break
        two = 0
        for i in reversed(a[:n-1]):
            if i % 2 == 0:
                two += i
                break
        for i in reversed(a[:n-1]):
            if i % 2 == 0 and two != i:
                two += i
                break
        print(max(one, two))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
