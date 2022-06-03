import sys
from itertools import permutations
input = sys.stdin.readline

"""

順列での組み合わせをしたとしても10の6乗程度なのでOK
その場合は全探索したほうが無難に回答が出せるので計算量の目安を考える

NGな対象のリストをどのように持つかわからなかったのと計算量を把握せずに進めたのが原因
対策は
・計算量をまず考える -> 低ければそのまま全探索での回答を考える
・リストのもたせ方を考える -> なにをどのように活用するか考える
-> 今回であればリストはif文で使用するのでbool型で持つべきだし
-> どの状態のときがNGなのかを把握して対応するべき

"""
runners = int(input())
runner_list = []
for i in range(runners):
    li = list(map(int, input().split()))
    runner_list.append(li)

ng = int(input())
ng_list = [[False] * runners for i in range(runners)]
for i in range(ng):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    ng_list[y][x] = ng_list[x][y] = True

pre_list = list(permutations(range(runners)))

ans = int(1e9)
flag = False
for i in pre_list:
    tmp = 0
    index = 0
    for j in range(runners):
        if j < runners - 1 and ng_list[i[j]][i[j+1]]:
            break
        tmp += runner_list[i[j]][j]
        index += 1
    if index == runners:
        ans = min(tmp, ans)
        flag = True

print(ans if flag else -1)
