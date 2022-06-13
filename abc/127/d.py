"""
嘘解法
全探索させちゃうけどプライオリティキューで高速化
※lambdaとheapqの直接インポートした結果AC

公式解説
すべての数字を混ぜてそこから大きいものを取得させる
※これのほうが簡単そう
"""

import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline
 
def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    heapify(A)
    li = []
    for _ in range(M):
        x, y = map(int, input().split())
        li.append((x, y))
    aftre = sorted(li, key=lambda x: -x[1])
    for i in range(M):
        for _ in range(aftre[i][0]):
            min_num = heappop(A)
            if min_num < aftre[i][1]:
                heappush(A, aftre[i][1])
            else:
                heappush(A, min_num)
                break
    print(sum(A))

main()
