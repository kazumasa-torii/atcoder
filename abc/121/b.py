"""
for一つで考える
"""
import sys
input = sys.stdin.readline
N, M, C = map(int, input().split())
B = list(map(int, input().split()))
li = [[] for _ in range(N)]
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        tmp[j] *= B[j]
        li[i].append(tmp[j])
ans = 0
tmp = 0
for i in li:
    tmp = sum(i) + C
    if tmp > 0:
        ans += 1
print(ans)
