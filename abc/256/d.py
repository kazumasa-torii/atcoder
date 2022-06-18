import sys
from typing import List
import bisect 
input = sys.stdin.readline
limit = (10 ** 5)
acc = [0] * limit
acc[1] = 0
for i in range(2, limit):
    acc[i] = acc[i-1] + i

def main():
    # N = int(input())
    # tmp = []
    # for _ in range(N):
    #     L, R = map(int, input().split())
    #     tmp.append(abs(acc[R] - acc[L]))
    tmp = [155, 255, 455]
    index = bisect.bisect_left(acc, sum(tmp))
    print(acc[index], sum(tmp), acc[index] - sum(tmp))
    index2 = bisect.bisect_left(acc, acc[index] - sum(tmp))
    print(acc[index2-1])
    return

main()
