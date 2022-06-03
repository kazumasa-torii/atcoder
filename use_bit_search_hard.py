import sys
input = sys.stdin.readline

N, W = map(int, input().split())
A = list(map(int, input().split()))

def judge(bit):
    S = 0
    for i in range(N):
        if bit & (1 << i):
            S += A[i]

    if S == W:
        return 1
    else:
        return 0

ans = 0

for bit in range(1 << N): # 0~32までやる（00000 ~ 11111 の 全探索）
    ans += judge(bit)

print(ans)
