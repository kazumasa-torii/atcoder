import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

# maxとminの数字を管理
mx = []
mn = []
cnt = defaultdict(int)

Q = int(input())

for _ in range(Q):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        x = tmp[1]
        cnt[x] += 1
        heapq.heappush(mx, -x)
        heapq.heappush(mn, x)
    if tmp[0] == 2:
        x, c = tmp[1:]
        cnt[x] = max(0, cnt[x]-c)
    if tmp[0] == 3:
        # 取り出したい値が０個の場合は続けてpopさせてリストから削除させる
        while cnt[-mx[0]] == 0:
            heapq.heappop(mx)
        while cnt[mn[0]] == 0:
            heapq.heappop(mn)
        # 最終的に残ったものは最小値は先頭に来ているのでlistで参照する
        print(-mx[0]-mn[0])
