import sys
from typing import List
import bisect
input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    # 累積和
    acc = [0]
    for i in range(1, N+1):
        acc.append(acc[i-1] + A[i-1])

    for _ in range(Q):
        q = int(input())
        k = bisect.bisect_left(A, q)
        if k >= N:
            k = N
        low = q*(k) - (acc[k] - acc[0])
        high = (acc[-1] - acc[k]) - q*(N-k)
        print(low+high)

    return

main()
