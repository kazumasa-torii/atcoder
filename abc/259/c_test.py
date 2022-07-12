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
abbaac
abbbbaaac

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    def rle(s):
        li = []
        li.append([s[0][0], 1])
        for c in range(1, len(s)):
            print(c)
            if len(s) > 0 and li[-1][0] == s[c]:
                li[-1][1] += 1
            else:
                li.append([s[c], 1])
        return li

    def solve(a, b):
        al = len(a)
        bl = len(b)
        if al != bl: return False
        for i in range(al):
            if a[i][0] != b[i][0]: return False
            int_a = a[i][1]
            int_b = b[i][1]
            if int_a == 1:
                if int_b != 1: return False
                else:
                    if int_b < int_a: return False
        return True

    S = input().strip()
    T = input().strip()
    s_list = rle(S)
    t_list = rle(T)
    print('Yes' if solve(s_list, t_list) else 'No')

    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
