import sys
input = sys.stdin.readline
H, W = map(int, input().split())
li = [list(input()) for _ in range(H)]
koma = []

for i in range(H):
    for j in range(W):
        if li[i][j] == 'o':
            koma.append([i, j])

ans = abs(koma[0][0] - koma[1][0]) + abs(koma[0][1] - koma[1][1])
print(ans)
