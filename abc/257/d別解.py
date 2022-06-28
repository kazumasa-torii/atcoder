from collections import deque

def dfs(N,G,start):
    dist = [-1] * N
    dist[start] = 0

    queue = deque([start])
    while queue:
#         now = queue.popleft() # bfs
        now = queue.pop() # dfs
#         print(now+1)
        for i in G[now]:
            if dist[i] != -1: continue
            queue.append(i)
            dist[i] = dist[now] + 1
        
    return dist

def is_ok(arg):
    G = [[] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if A[i][2]*arg >= len_list[i][j]:
                G[i].append(j)
    for i in range(N):
        dist = dfs(N,G,i)
#         print(dist)
        if -1 not in dist:
            return True
    return False


def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

N = int(input())
A = [[]for i in range(N)]
for i in range(N):
    A[i] = list(map(int, input().split()))
# print(N,A)
len_list = [[0 for i in range(N)]for j in range(N)]
for i in range(N):
    for j in range(N):
        len_list[i][j]= abs(A[i][0]-A[j][0])+abs(A[i][1]-A[j][1])
# for i in range(N):
#     print(*len_list[i])

ans = meguru_bisect(-1,5*10**9+2)

print(ans)
