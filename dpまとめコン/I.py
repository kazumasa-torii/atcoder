"""
確率DPを行う
基本は表のみの状態を保持しておくので裏の可能性は研鑽で求まるので無視

埋める配列
dp[i][j] := 最初の i 枚のコインを投げたときに、表が j 枚となる確率

緩和式
次のコインが表のとき: dp[i+1][j+1] += dp[i][j] * p
次のコインが裏のとき: dp[i+1][j] += dp[i][j] * (1 - p)

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
5
0.42 0.01 0.42 0.99 0.42

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    p = list(map(float, input().split()))
    dp = [[0] * (3100) for _ in range(3100)]
    dp[0][0] = 1.0

    for i in range(n):
        for j in range(n+1):
            dp[i+1][j] += dp[i][j] * (1 - p[i])
            dp[i+1][j+1] += dp[i][j] * p[i]

    ans = 0
    for i in range(n+1):
        if n - i < i: ans += dp[n][i]
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
