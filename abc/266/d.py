"""
DPですよー

DP[x][t] =
    高橋君が時刻 t に
    座標 x にいるときの、
    それまでに捕まえたすぬけ君の大きさの合計の最大値

以下遷移

DP[x][t]=
    max(
        DP[x-1][t-1],
        DP[x][t-1],
        DP[x+1][t-1]
        )
    +時刻 t に座標 x にいることで捕まえることができるすぬけ君の大きさ

"""

import sys
input = sys.stdin.readline
def main():
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    max_time = 0
    for i in li: max_time = max(i[0], max_time)
    position_list = [0] * (max_time + 1)
    scor_list = [0] * (max_time + 1)

    for i in li:
        t, x, a = i
        position_list[t] = x
        scor_list[t] = a

    dp = [[-int(1e19)] * (max_time + 1) for _ in range(5)]
    dp[0][0] = 0

    # 遷移は時間経過ごとに座標の各位置のmaxを取っておいてその内容にて更新する
    for time in range(1, max_time+1):
        for position in range(5):
            dp[position][time] = dp[position][time-1]
            if position != 0: dp[position][time] = max(dp[position][time], dp[position-1][time-1])
            if position != 4: dp[position][time] = max(dp[position][time], dp[position+1][time-1])

        dp[position_list[time]][time] += scor_list[time]
    print(max(dp[i][max_time] for i in range(5)))
    return

if __name__ == '__main__':
    main()
