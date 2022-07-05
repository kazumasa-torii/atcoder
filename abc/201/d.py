import sys
sys.setrecursionlimit(3000)
def f(i, j):
    if i == H-1 and j == W-1: return 0
    if visited[i][j]: return memo[i][j]

    visited[i][j] = True
    res = -10 ** 10
    if j + 1 < W:
        res = max(res, score[i][j+1] - f(i, j+1))
    if i + 1 < H:
        res = max(res, score[i+1][j] - f(i+1, j))
    memo[i][j] = res
    return memo[i][j]

if __name__ == "__main__":
    H, W = map(int, input().split())
    s = [list(input()) for _ in range(H)]
    score = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            score[i][j] = 1 if s[i][j] == '+' else -1
    visited = [[False] * 2005 for _ in range(2005)]
    memo = [[0] * 2005 for _ in range(2005)]

    ans = f(0, 0)
    if ans == 0: print('Draw')
    if ans < 0: print('Aoki')
    if ans > 0: print('Takahashi')
