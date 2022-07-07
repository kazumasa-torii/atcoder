"""
二分探索と累積和
"""
import sys
input = sys.stdin.readline

def main():
    def judge(acc):
        for row in range(K, N + 1):
            for col in range(K, N + 1):
                cnt = acc[row][col] - acc[row - K][col] - acc[row][col - K] + acc[row - K][col - K]
                if cnt < K ** 2 // 2 + 1:
                    return True
        return False

    def twoDimensionsAcc(mid):
        acc = [[0] * (N + 1) for _ in range(N + 1)]
        for row in range(N):
            for col in range(N):
                if A[row][col] > mid:
                    acc[row + 1][col + 1] = 1

        for row in range(1, N + 1):
            for col in range(N):
                acc[row][col + 1] += acc[row][col]

        for col in range(1, N + 1):
            for row in range(N):
                acc[row + 1][col] += acc[row][col]
        return acc

    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    ok = 10 ** 10
    ng = -1

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        acc = twoDimensionsAcc(mid)

        if judge(acc):
            ok = mid
        else:
            ng = mid

    print(ok)
    return

if __name__ == '__main__':
    main()
