import sys
input = sys.stdin.readline

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    k = 10
    dp = [[0] * (k+1) for _ in range(n+1)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(k):
            if dp[i][j] == 0: continue
            dp[i+1][j] = max(dp[i+1][j], 0) + dp[i][j]
            dp[i+1][(j+a[i])%2] = max(dp[i+1][(j+a[i])%2], 0) + dp[i][j]
    print(dp[-1][p]) 
    return

if __name__ == '__main__':
    main()