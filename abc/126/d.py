"""
偶数、奇数としてだけ理解して対応する
なので1,0だけで判断させる

木の頂点までの表し方が肝
"""

from collections import deque

N = int(input())

G = [[] for _ in range(N)]
for _ in range(N-1):
    u,v,w = list(map(int,input().split()))
    w%=2
    u-=1
    v-=1
    G[u].append([w,v])
    G[v].append([w,u])

ans = [-1] * N
ans[0] = 1

que = deque([(0,0)]) #weight,pos
while que:
    d, curr = que.popleft()
    for w, nxt in G[curr]:
        if ans[nxt]==-1:
            ans[nxt] = (ans[curr] + w)%2
            que.append((ans[nxt],nxt))

for a in ans:
    print(a)
