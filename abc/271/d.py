import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def main():
    n, s = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(n)]
    dp = [[[-1,''] for _ in range(s+1)] for _ in range(n+1)]
    dp[0][0][0] = 0
    for i in range(n):
        for j in range(s):
            if dp[i][j][0] == -1: continue
            if dp[i][j][0] + nums[i][0] <= s:
                dp[i+1][j + nums[i][0]] = [dp[i][j][0]+nums[i][0], dp[i][j][1]+'H']
            if dp[i][j][0] + nums[i][1] <= s:
                dp[i+1][j + nums[i][1]] = [dp[i][j][0]+nums[i][1], dp[i][j][1]+'T']
    if dp[-1][s][0] != -1:
        print('Yes')
        print(dp[-1][s][1])
    else:
        print('No')
    return

if __name__ == '__main__':
    main()