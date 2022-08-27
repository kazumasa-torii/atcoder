import sys
input = sys.stdin.readline
def main():
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    max_time = 0
    for i in li: max_time = max(i[0], max_time)
    X = [0] * (max_time + 1)
    A = [0] * (max_time + 1)

    for i in li:
        t, x, a = i
        X[t] = x
        A[t] = a

    dp = [[-int(1e19)] * (max_time + 1) for _ in range(5)]
    dp[0][0] = 0

    for time in range(1, max_time+1):
        for position in range(5):
            dp[position][time] = dp[position][time-1]
            if position != 0: dp[position][time] = max(dp[position][time], dp[position-1][time-1])
            if position != 4: dp[position][time] = max(dp[position][time], dp[position+1][time-1])
        dp[X[time]][time] += A[time]
    print(max(dp[i][max_time] for i in range(5)))
    return

if __name__ == '__main__':
    main()
