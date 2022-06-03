#input
import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
z = [[] for _ in range(N)]
# graph作成
for _ in range(M):
    x, y = map(int, input().split())
    z[x-1].append(y-1)

# メモ化再帰用のメモを作成
memo = [False] * N

# そこから行ける最大値を格納していく
max_num_list = [0] * N

def dfs(v):
    if memo[v]:
        # 始まりがここからだと最大値以上増えないのでlistの数値を返す
        return max_num_list[v]
    else:
        res = 0
        # 再帰的に探索
        for u in z[v]:
            res = max(res, dfs(u)+1)
        max_num_list[v] = res
        memo[v] = True
        return res

# graphの頂点iをすべて始める（どの頂点からスタートするのが最大化になるか探索するため）
for i in range(N):
    dfs(i)

print(max(max_num_list))
