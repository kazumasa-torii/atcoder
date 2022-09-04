import sys
input = sys.stdin.readline
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    dp = [[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            dp[i][j] += a[j] * (i+1)
    ans = 0
    idx = -1
    for i in range(m-1, -1, -1):
        ans += dp[i][idx]
        idx -= 1
    print(ans)
    return

if __name__ == '__main__':
    main()