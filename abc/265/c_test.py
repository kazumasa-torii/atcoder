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
9 44
RRDDDDRRRDDDRRRRRRDDDRDDDDRDDRDDDDDDRRDRRRRR
RRRDLRDRDLLLLRDRRLLLDDRDLLLRDDDLLLDRRLLLLLDD
DRDLRLDRDLRDRLDRLRDDLDDLRDRLDRLDDRLRRLRRRDRR
DDLRRDLDDLDDRLDDLDRDDRDDDDRLRRLRDDRRRLDRDRDD
RDLRRDLRDLLLLRRDLRDRRDRRRDLRDDLLLLDDDLLLLRDR
RDLLLLLRDLRDRLDDLDDRDRRDRLDRRRLDDDLDDDRDDLDR
RDLRRDLDDLRDRLRDLDDDLDDRLDRDRDLDRDLDDLRRDLRR
RDLDRRLDRLLLLDRDRLLLRDDLLLLLRDRLLLRRRRLLLDDR
RRRRDRDDRRRDDRDDDRRRDRDRDRDRRRRRRDDDRDDDDRRR

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    def dfs(x, y):
        if x < 0: return [x+1, y]
        if x >= h: return [x-1, y]
        if y < 0: return [x, y+1]
        if y >= w: return [x, y-1]
        if memo[x][y]: return [-1, -1]
        memo[x][y] = True
        tx, ty = dic[maps[x][y]]
        x += tx
        y += ty
        return dfs(x,y)
    h, w = map(int, input().split())
    maps = [input() for _ in range(h)]
    memo = [[False] * w for _ in range(h)]
    dic = {'U':[-1, 0], 'D':[1, 0], 'R':[0, 1], 'L':[0, -1]}
    ans = dfs(0, 0)
    if ans[0] != -1 and ans[1] != -1:print(ans[0]+1, ans[1]+1)
    else:print(-1)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
