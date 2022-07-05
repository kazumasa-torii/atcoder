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
xxxxx?xxxo

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    S = list(input())
    l = len(S)
    ab = []
    no = []
    cnt = 0

    for i in range(l):
        if S[i] == 'o':
            cnt += 1
            ab.append(i)
        if S[i] == 'x':
            no.append(i)
    if cnt > 4:
        print(0)
        return
    ans = 0
    for i in range(10**4):
        tmp = list(str(i).zfill(4))
        flag = True
        for a in ab:
            if str(a) not in tmp:
                flag = False
                break
        for n in no:
            if str(n) in tmp:
                flag = False
        if not flag:
            continue
        ans += 1
    print(ans)
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
