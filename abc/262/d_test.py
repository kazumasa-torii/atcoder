"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
5
5 5 5 5 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #dpテーブルのshapeは（割る数,余りのパターン数,採用数）
    dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(1,N+1)]
    # N個目のデータを取り出す
    for i in range(N):
        # 割る数
        for n in range(1,N+1):
            amari = A[i] % n
            # 採用数方向
            for k in reversed(range(N)):
                if k == 0:
                    dp[n-1][amari][0] += 1
                else:
                    # 既存のあまりの数
                    for a in range(N):
                        dp[n-1][(a+amari)%n][k] += dp[n-1][a][k-1]
                        dp[n-1][(a+amari)%n][k] %= 998244353
    ans = 0
    for i in range(N):
        ans += dp[i][0][i]
        ans %= 998244353
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
