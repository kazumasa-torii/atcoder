def solve(x):
    rem = N
    # tは秒
    for t in range(10 ** 8):
        if C[x][t % 10] > 0:
            C[x][t % 10] -= 1
            rem -= 1
        if rem == 0:
            return t


N = int(input())
S = [input() for _ in range(N)]

# 出現場所を取得
C = [[0] * 10 for _ in range(10)]

for i in range(N):
    for j in range(10):
        C[int(S[i][j])][j] += 1

print(min(solve(i) for i in range(10)))
