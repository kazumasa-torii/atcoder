"""
これ復元が難しい
復元のやり方は
"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
abracadabra
avadakedavra

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)

    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    ml = dp[n][m]
    ans = [str() for _ in range(ml)]

    while ml > 0:
        if s[n-1] == t[m-1]:
            ans[ml-1] = s[n-1]
            ml -= 1
            n -= 1
            m -= 1
        elif dp[n][m] == dp[n][m-1]:
            m -= 1
        else:
            n -= 1

    print(''.join(ans))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
