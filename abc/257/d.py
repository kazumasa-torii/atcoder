"""
ワーシャルフロイド版
"""
def main():
    N = int(input())
    L = []

    for i in range(N):
        x, y, P = list(map(int, input().split()))
        L.append([x, y, P])

    inf = 10 ** 10
    wf_L = [[inf] * N for i in range(N)]

    for start in range(N):
        sx, sy, sp = L[start]
        for goal in range(N):
            if start == goal:
                wf_L[start][goal] = 0
            else:
                gx, gy, gp = L[goal]
                length = abs(sx - gx) + abs(sy - gy)
                S = -(-length // sp)
                wf_L[start][goal] = S

    for mid in range(N):
        for start in range(N):
            for goal in range(N):
                wf_L[start][goal] = min(wf_L[start][goal], max(wf_L[start][mid], wf_L[mid][goal]))

    ans = inf
    for tmp in wf_L:
        ans = min(ans, max(tmp))
    print(ans)

if __name__ == '__main__':
    main()
