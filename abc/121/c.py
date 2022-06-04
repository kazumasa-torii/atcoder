"""
まずはsortして解決できないか考える
その上でDPまたはDFS、BFSが必要ならば使う
二分探索木もあるよ
"""
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
li = []
for _ in range(N):
    cost, size = map(int, input().split())
    li.append([cost, size])
over_li = sorted(li , key=lambda x:x[0])
ans = 0
for cost, size in over_li:
    if size <= M:
        ans += cost*size
        M -= size
    else:
        ans += cost*M
        M = 0
    if M == 0:
        break
print(ans)
