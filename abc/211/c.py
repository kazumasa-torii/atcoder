import sys
input = sys.stdin.readline
def main():
    mod = 10 ** 9 + 7
    s = input().strip()
    n = len(s)
    t = 'chokudai'
    dp = [[0] * 9 for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(n):
        for j in range(8):
            if s[i] != t[j]:
                dp[i+1][j+1] = dp[i][j+1]
            else:
                dp[i+1][j+1] = (dp[i][j+1] + dp[i][j]) % mod
    print(dp[n][8])
    return

if __name__ == '__main__':
    main()
